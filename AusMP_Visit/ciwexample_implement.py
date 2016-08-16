>>> params = {'Arrival_distributions': [['Exponential', 6.0],
...                                     ['Triangular', 0.05, 0.8, 0.9]]
...           'Service_distributions': [['Weibull', 0.8, 0.9],
...                                     ['Lognormal', 4.5, 2.0]],
...           'Transition_matrices': [[0.0, 0.6],
...                                   [0.3, 0.1]],
...           'Number_of_servers': [4, 'Inf']}




>>> import ciw
>>> ciw.seed(6)
>>> N = ciw.create_network(params)
>>> Q = ciw.Simulation(N)
>>> Q.simulate_until_max_time(2000)
>>> recs = Q.get_all_records()