>>> import ciw
>>> params = {
...   'Number_of_nodes': 2,
...   'Arrival_distributions':
...      [['Exponential', 6.0],
...       ['Uniform', 0.2, 0.4]],
...   'Service_distributions':
...      [['Lognormal', 0.4, 0.3],
...       ['Deterministic', 0.25]],
...   'Transition_matrices':
...      [[0.5, 0.1],
...       [0.0, 0.4]],
...   'Number_of_servers': [3, 1],
...   'Simulation_time': 2000}
>>> Q = ciw.Simulation(params)
>>> Q.simulate_until_max_time()
>>> recs = Q.get_all_records()
