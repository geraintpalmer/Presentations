params = {
  'Number_of_nodes': 2,
  'Number_of_classes': 2,
  'Number_of_servers': [3, 1],
  'Simulation_time': 2000,

  'Arrival_distributions':{
    'Class 0': [['Exponential', 6.0],
                ['Uniform', 0.2, 0.3]],
    'Class 1': [['Lognormal', 0.4, 0.3],
                ['Deterministic', 0.25]]},

  'Service_distributions':{
    'Class 0': [['Exponential', 7.0],
                ['Deterministic', 0.3]],
    'Class 1': [['Exponential', 7.0],
                ['Exponential', 4.5]]},
                
  'Transition_matrices':{
    'Class 0': [[0.0, 0.5],
                [0.0, 0.8]],
    'Class 1': [[0.2, 0.0],
                [0.2, 0.4]]}
}