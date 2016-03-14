>>> import ciw
>>> params = {'Number_of_nodes': 1,
...           'Arrival_distributions': [['Exponential', 6.0]],
...           'Service_distributions': [['Exponential', 5.0]],
...           'Transition_matrices': [[0.5]],
...           'Number_of_servers': [1],
...           'Queue_capacities': [3],
...           'Detect_deadlock': True}
>>> Q = ciw.Simulation(params)
>>> times_to_deadlock = Q.simulate_until_deadlock()
>>> times_to_deadlock[((0, 0),)]
1.1707879982560288
