Queues are all around us. People wait to buy their sandwiches in the maths cafe, to be seen by a doctor at A&E. Modelling these queueing systems can give us better understanding of the services around us: what if we invest in another bed the in Heath hospital? Or remove the contactless machine in the maths cafe? How will that effect waiting times?

A popular way of modelling queues is through computer simulation. That is, building a virtual copy of that system, full of its rules and interconectedness, inside a computer. And then we let virtual people run wild and interact with it. In my PhD, I've built a Python package that allows you to do just that in only a few lines of code.

Consider the system here: like the news keeps telling us, our hospital ward is full. And like the news keeps telling us, community care services are also full.
Now my nan Sheila is ready to leave hospital, but she can't until she's admitted to community care services, which are full. She remains in her hospital bed until room becomes available. Bedblocking.
All the while my aunty Barbera is having community care but needs to go to hospital, but its full. Her community workers are just trying to keep her ticking over until the hospital can take her.

Now Sheila is waiting for Barbera to move so that she can leave hospital.
And Barbera is waiting for Sheila to move so she can enter hospital.
We have a deadlock.

Now in reality the hospital and community workers speak to each other, and they can just swap Sheila and Barbera. In a computer simulation model, that's not so trivial. How does a computer know Sheila and Barbera are waiting on each other? How does it know the system is in deadlock?

In my Phd I developed a method of detecting deadlock in computer simulations of queueing systems. We can represent the system as a graph; where vertices correspond to servers, and edges correspond to blockage relationships. Now our system is in deadlock if and only if its graph representation contains a knot: that is a set of vertices inescapable by travelling along the edges.
This now allows our computer simulations to better represent reality, and allows us to model more complex systems.

I've been using simulation to model a real healthcare system in Gwent, evaluating the effect of a new healthcare intervention. This delivers valuable insights into demand, workforce requirements and costs, for our hardworking heroes of the NHS.

Thank you.