I am a PhD student at Cardiff University researching the mathematics of queueing networks, and simulation. In my work I mainly use Python for all numerical experiments, simulations, and data analysis. Over the course of this programme I developed the Python library Ciw for the simulation of queueing systems. I have given talks at Python conferences before, namely PyCon UK 2016, PyCon Namibia 2016 and Python Namibia 2015, these talks, amongst more mathematical talks can be found here: http://www.geraintianpalmer.org.uk/talks/






# Producing Pretty Plots in Python

Plots are awesome. In one image they can say what paragraphs of descriptive text can't. They are the standard and go-to way of presenting data findings in all walks of life, from scientific journals to tabloid newspapers. They are an important graphical technique in statistics and mathematics, and an exploratory tool for data analysis.

Matplotlib is an extremely powerful tool for producing informative, useful, and beautiful visualisations. This power intensifies when combined with libraries such as Numpy, Scipy, and Seaborn, and tools like Jupyter Notebooks, creating an essential toolbox for data visualisation in Python.

In this talk, through numerous examples, I will present some of my methods for creating pretty plots in Python, and discuss appropriateness of various types of plots. Plots will be built up adding levels of detail gradually, manipulating gridlines, annotations, ticks, colormaps, labels, and other plot components to produce high quality and descriptive data visualisations in Python.





# Queueing and Python: pip install ciw

Queueing systems dominate our day-to-day life: for example supermarkets, airports, traffic systems, and call centres, naming only a few obvious examples. A better understanding of these queues can help businesses and service providers optimise these systems, improving efficiency, profit and satisfaction levels. Sometimes some unintuitive behaviour can arise, and so modelling and investigating queues mathematically has become very popular and important. One prominent method of doing so is by using computer simulation.

This talk will present Ciw, a new Python library for simulating open queueing networks. This talk will demonstrate using Ciw's simple interface to model and simulate a queueing system, and an overview of it's many features will also be given.

The library is currently being used in two academic settings: one theoretical project that investigates queueing networks that deadlock, and another practical project in which patient flows are modelled in an ophthalmology clinic. Synopses of these projects and their results will be discussed.




# Analysing and Modelling Cancer Diagnostics in Wales

This is a joint piece of work with Professor Paul Harper, and the oncology department at Cwm Taf Health Board, Wales.

The 28 day target from initial suspicion to cancer diagnosis is seldom met in the Cwm Taf region. This projects uses Python, especially Pandas and Matplotlib for data analysis, identifying worst performing cancer sites, and potential bottlenecks in the diagnostic process. The work also models the diagnosis process as a queueing network, and uses Ciw, the queueing network simulation library, to simulate the system. Scenarios can then be run, for example would a 20% increase in MRI scanning capacity aid in getting within the 28 day target?

This project uses a combination of data analysis and operational research methods, all implemented in Python. It is also an example of how we can deal with minimal information when building and executing models of real world systems.