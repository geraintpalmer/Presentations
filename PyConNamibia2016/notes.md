# Simulating Queues with Ciw

Hi, I'm Geraint. This will be a kind of 2-in-1 talk, first about the library Ciw, and second about how I went about building the library.

---

Firsty, what is a queue?
It's some sort of service centre in which customers arrive, spend some time in service, and then leave.
In some queues if there are already a certain number of customers already in service, the next customer cannot begin service immediately, and so must wait in line until servers become available. We get lines of people waiting like this.

So why do we study queues?

I'm sure around campus this week you've seen scenes like this all over the place. Is there anything we can do to optimise this? Reduce waiting times? Minimise the space required to queue?
Does big queues put customers off using your business?
In a call center maybe a queueing customer is costing you money?
How about waiting lists in a hospital?

Studying queues can give insight into optimisation methods, and simulation is one of doing this.

---

This a a simulation.

It's a representation of a system (real or otherwise).
There are rules in order to accurately represent that system. For example superman doesn't fly to the fron of the queue.
And key performance indicators and what-if scenarios can be carried out.

Now the performance indicators in this example could be a rough instinct of how long the queue will get. What if scenarios may be adding extra servers, of speeding up service.

However modelling like this is inaccurate, time-consuming, and can be expensive (buying all the lego for example, hiring staff to play with it).

This is where computer simulation comes in.

---

Mathematically, the simplest queue to consider is an M/M/1 queue shown here.
In this queue, customers arrive randomly according to the Poisson distribution (that is their inter-arrival times are random according to the exponential distribution), there is only one server, and service times are random according to the exponential distribution.

Imagine if customer arrive randomly 4 every hour, and services take roughly every 15 minutes. We don't expect any queue right? Let's use the library Ciw to find out.

---

DEMO

---

The library Ciw specialises in simulating networks of queues, represented here.
Once a customer finishes service that customer has probabilities of joining other queues in the network.
These service centres are called nodes.

Here you can see various features such as multiple servers, and limited queueing capacities.
In this case if a customer wishes to enter that node when it is full, that customer if blocked, remaining tied to its server until it may enter the next node when room becomes available. That tied server meanwhile cannot server any other customer waiting at that node.

---

Here's an overview of the library, now to talk about the code itself.

---

Ciw uses the 3 phase simulation approach shown in this flow diagram.
Start at the start, and initialise the system.

At phase A the clock is moved forward to the next scheduled event.
At phase B the scheduled events are carried out. This may tigger unscheduled events that need to be carried out immediately.
These are carried out in phase C.
Again these may trigger more unscheduled events to be carried out, so we check if there is any more C event, and then go back ancarry them out.
Once there is no more events to be carried out at that time point, we check if the simulation has ended (that is reach its maximum time). If not, we go back to A and move the clock forward. Else end the simulation.

---

For a queueing network, what are scheduled events?
	-  A customer arriving from outside the system
	-  Someone completing service
The unscheduled events?
	- A customer beginning service
	- A customer being released (moving to next node, out leaving system)
	- A customer getting blocked

For example, an external customer, Fiona, joins a queue, but may not begin service immediately (they have to wait).
Then a customer at that node, Alvin, finishes service. This triggers a release, Alvin moves to another node. This triggers Fiona to be able to begin service.

---

This all requires an important concept, sampling from a distribution.
Say service times follow a lognormal distribution, as shown. We want to choose random service times, such that when they ar plotted as a histogram it resembles the lognormal curve.

SHOW GIF

---

The code itself is all object orientated and structured as follows, with Individuals moving from Node to Node carrying around dictionaries of DataRecords.
Two special nodes are show, the ArrivalNode that spawns new external customers, and the ExitNode that collects all customers that leave the system.

So how did it all develop?

---

It began with me learning to code, and doing a lot of pair programming and collaborative work.
This I fell was invaluable to be and one of the best ways to learn anything!

The photos show some important concepts:
	- Sharing a screen and discussion
	- Working through tutorials together
	- Stepping away from a keyboard and screen, and planning out code using a white board.

---

Version control with Git and collaborative work on GitHub is the backbone of the project.
I won't talk too much about this as there's a workshop on it at some point.

---

One feature I do want to emphasise is GitHub Issues, this helped me keep track of ideas and what needed to be done, and also to prioratise what I was working on. The colour-coded labelling system was particularly useful.

---

Tests! Testing the library was extremely important, how did I know the code worked?!
I began hating tests, but now won't commit any code without them!

---

I began my testing journey with doctests like this, writted into the code itself.
This was a great intro to testing, simple:: if I run this bit of code, what do I expect to be spat out?
Floating point numbers did have to be rounded like so to be consistant on all computers.

As the code grew, this quickly made the code messy. Although I still use docetsts to test documentation.

---

Next came unittests, which are more formal.
I like that I can compare the output of two equivalent functions etc.
And I now had a seperate file full of test scripts.

I've also been introduced to hypothesis testing, which David will speak about later on.

---

I also use Travis to automatically assert whether tests pass or not whenever I get pull requests.
You'll get a nice green badge if you've been good!

---

Now comes my new most favourite thing ever: coverge!
OK, my tests pass, but are the tests actually testing the code?
Coverage tells me how may lines of my code are run when tests are run.
And its as simple to run as this!

---

You get a nice report like this.
And whatever coverage tells you, its good news!
Either you have 100% coverage, yay! Or, you haven't covered this line, test if it works or if it is needed.

It even tells you what lines haven't been covered by tests!

And its a glorious feeling hitting 100%!

---

Packaging quickly. Until recentlyI didn't know what this was really.
But now with some packagin magic, Ciw is on PyPI for everyone to install!

---

And documentation was very important to me, especially working with others.
A student from the netherlands has been using this code in her studies, it would've been inpractical to explaing everything to her enough times that she could use it independently.

---

I used Sphinx to create documentation, and is hosted at ciw.readthedocs.org

SHOW DOCS

Hopefully I've written nice clear instructions and tutorials for anyone to get started with Ciw, and any other features of Ciw that are required. (such as server schedules, custom distributions, etc.)

---

So the library is currently being used in to academic projects::
	- A theoretical work on deadlock in queueing networks by myself, Vince and Professor Paul Harper
	- And a practical use to model an opthamology clinic by Lieke Holscher and Dr Jennifer Morgan.

---

This queueing network is in deadlock.
The customer at A1 cannot eneter its destination until theses customers have moves, and they cannot enter their destination until the customer at A1 has moved. Its Catch-22.

Through this research Ciw now has capability to detect deadlock situations using a state-digraph, in which a knot highlights when deadlock occurs. Time until deadlock can be recorded.

---

The work compared simulation results to analytical results, yielding my favourite graph: maths and simulation line up perfectly, and we get interesting behaviour as service rate increases.

---

Lieke's practical work was looking at three clinics with various opening times. The server schedule feature of Ciw was developed specially for this work.

Here patients eneter accordign to a schedule, are serverd when the clinic is open, and may get told to come back in a month, 6 months or a year. She's looking into how arrival strategies can effect demand on the system.

---

I hope you found that interesting, and if you'd like to use or contribute to Ciw, please do! Thanks!