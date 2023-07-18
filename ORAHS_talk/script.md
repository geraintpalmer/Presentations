Hello, my name is Geraint Palmer, and I am speaking today about a project undertaken by a team of us at Cardiff University on modelling and optimising ambulance fleet allocations in Jakarta, Indonesia. This work is funded by the UKRI's Global Challenges Reasearch Fund, and is done in collaboration with 118: an ambulance charity within Jakarta, and 119: an Indonesian government funded ambulance service in the country.

---

Indonesia is an archipelago country in South East Asia, and is the 4th most populated country in the world. It's capital is Jakarta 2nd most populated urban area in the world, with 34 million inhabitants.

Such a city poses numerous problems for the efficient running of a city wide ambulance service. One problem is that this is what the roads look like: traffic is crazy, and there also isn't really a culture out there for prioritising ambulances over other vehicles. So trust in the service is low, and people in emergencies tend to want to make their own way to a hospital, at great risk to their own health, meaning that demand for the service is actually a lot lower that what they'd like it to be.

So working with our Indonesian partners, there were some questions to answer:
 + Given their current fleet, how should they distriubute the ambulances around the city?
 + If they were able to increase demand, how much resources would they require?

---

Breaking down ans simplifying the problem: patients can be split into three specialties:
  - A1: patients needing immediate life-saving assistance
  - A2: other emergency patients
  - B: non-emergency patients
As you can see from these maps, demand is very location dependant.

The services there have two types of vehicle:
 - Primary vehicles, which are the emergency ambulances. All patients require one of these.
 - Secondary vehicles, which are also called rapid responce vehicles. These are bikes that can travel faster and whip between traffic, and provide medical assistance on the scene, but cannot transport patients. There are sent out for A1 and A2 patients if they can reach the patient before the primary vehicle.

There are 67 ambulance stations spread across the city. The question is where should be put all the vehicles? We'd like to produce an allocation like this, that optimises... something.

There are various things we could optimise for, e.g. average reponse time or coverage. We decided to look at probability of surviving.

---


We do this through survival functions, which are models that, for each different speciality of patient, predicts the probabilty of surviving based on response time.
  - These could naivly be cutoffs: if reached in under 8 minutes they survive, if over 8 minutes they don't;
  - Or they could be something more sophisticated, like this exponentially decreasing chance of survival.
We decided to use a mixture of these for the different specialities, based on the evidence at hand. We use this survival surve for A1 patients, a 15 minute cutoff for A2, and a 60 minute cutoff for B patients.

---

The idea then is to combine optimisation and simulation.
 - an optimisation model is built. This takes in data about the situation in Jakarta, and some hyperparameters, and produces an optimised allocation for primary and secondary vehicles that maximises survival.
 - a simulation model then evaluates this allocation producing other useful KPIs such as response time distributions.

---

The objective of the optimisation maximises survival. We call this a "Maximum Expected Survival Location Model with Heterogeneous Patients and Heterogeneous Fleets", or MESLMHPHF. Here it is. It sums up the expected number number of patients surviving for each speciality: those potentially having 2 vehicles, and those requiring one vehicle.
We get those numbers by multiplying demand by each individuals probability of surviving, given each vehicle location. And summing across vehicle locations and pickup locations.

---

To get those probabilities: If we look just at the top equation, that's the probabilty of being seen by an ambulance at location a, and surviving, given you're a speciality that only needs one vehicle, at pickup location p.

To get this we take
 - the probability of surviving, from the survival function and the travel time between a and p
 - multiplied by the probabilty that that primary vehicle isn't busy
 - multiplied by the probability that all closer primary vehicles are busy

Then for patients that can also be seen by secondary vehicles, we sum together their survival from being seen by a primary and secondary vehicles, but now with the added restriction that all closer vehicles of either type need to be busy too.

A key part of these equations, is these pi's. They represent the utilisation of vehicles in each vehicle location. But, thise utilisations themselves are allocation dependant. So before we can use this we need to find out what those are.

---

By considering utilisation as demand rate over service rate, like we do in queueing theory, then we can write down implicit equations relating the demand experience by each vehicle location. We don't think we can solve these analytically, but we can solve them numerically by finding roots using Powell's method. And SciPy does this for us.

---

So for a given allocation, we can find the vehicle utilisations, and then the expected survival. As the this isn't linear, we then use this as an objective function in a heuristic algorithm to find the best allocation. We use a population based simulated annealing approach, and here's a representation of that, we see the line go up which is good.

The particular heuristic here isn't really a concern for us and more sophisticated heuristics could be used. But we are only running this once so we don't really mind. The objective function can be vectorised, so the only thing that takes time is solving for the utilisations.

---

So we end up with some allocation that maximises survival. But how well does it perform on other metrics, e.g. response times? For this we build a discrete event simulation in the Python library Ciw. This now allows us to test the allocation on a slightly more realistic system, with time dependant demand and traffic levels or travel times.

We model this as a queueing system, where 'ambulance jobs' are the customers, and 'ambulances' are the servers, with jobs routed to the closest ambulance. We simulate primary and secondary vehicles separately, and sequentially, feeding the complete output of one as input to the other.

---

For primary vehicles, an ambulance job consists of travelling from the ambulance location to a pickup location, spending time giving treatment at the pickup location, travelling to a hospital, spending time handing the patient over, travelling back to the ambulance locations, and spending time refilling and refueling the vehicle. So the service time of an ambulance job is calculated by sampling each of these travel times and delays, and summing them.
There is also a probability of not needing a hospital and travelling back straight away.


A neat thing here is the hierarchical behaviour between the vehicle types: primary vehicles behave independently of secondary vehicles, and secondary vehicles just react to the primary vehicle behaviours. Therefore we can simulate primary vehicles first, then secondary vehicles in a second sequential simulation.

The output of the primary vehicle simulation is a record, for every ambulance job, of the timestamps where each journey segement started and finished. This is fed into a second simulation, simulating the logic of the secondary vehicles. Secondary vehicles react to how primary vehicles behaved, e.g.:
- in the primary simulation a call arrives, and primary vhicles arrives at the pickup location and then leaves with the patient. If the patient is of a speciality that would require a secondary vehicle, then we identify the closest secondary vehicle, and its behaviour depends on the primary vehicle:
  - they could arrive before the primary vehicle and remain with the patient until they leave for the hospital
  - they could arrive after the primary vehicle and remain with the patient until they leave for the hospital
  - they could arrive after the primary vehicle has left and return straight home.

In this way there is no synchronicity issues between the two simulations, and each patient recieves a response time, the minimum between the time the primary and secondary vehicle reached them.

We can then record some KPIs such as mean response times, vehicle utilisations, and percentage of calls abandoned as no ambulance was available.

---

Comparing the currently used allocation and that obtained by the optimisation algorithm, for 81 primary and 13 secondary vehicles, we see the following KPIs.
The expected maximum survival increases as expected, even though mean response time worsens, indicating it isn't a very good proxys for measuring survival. It's interesting to see that ambulance utilisation increases slightly, but RRV utilisation decreases significantly, indicating that this improved allocation changes the vehicle behaviours too.

---

Finally, as mentioned before, the demand for the ambulance service in Jakarta is much lower than we would expect to see in Europe. A previous study showed a numebr of reasons for this, including visibility, reliability and cost. We devised 3 new demand scenarios, along with the current to model, that reflect addressing each of these. So here the columns represent an increasing proportion of emergency patients using the service.

We re-ran the optimisations and simulations for each of these, obtaining new allocations and corresponding KPIs each time. And out results show that as demand rises, all KPIs worsen when there is no change in resource level. We are currently working on finding what extra resource levels would be required to maintain an acceptable, or at least maintain the current KPIs.

---

So in summary:
  + we have formulated a maximal survival objective function that accounts for heterogeneous patients and multiple vehicels
  + it also addresses the circular nature of the utilisations,
  + and we built a simulation model of the ambulance behaviour.

These will advice out Indonesian partners to be able to better plan and prepare their ambulance service.

Next we will be:
  + considering what resource levels are required for different demand scenarios

And future work could look at:
  + considering that service rates are also location and allocation dependant, like the utilisations;
  + and possibly replicating the work in a very different setting, with the Welsh Ambulance Service.

Thank you.





