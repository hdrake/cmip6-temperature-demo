# cmip6-temperature-demo

## A handful of tutorials for basic analysis of climate models from CMIP6 on the Google Cloud Platform

#### Analyzing state-of-the-art simulations of global warming (historical and future projections)

The following binder is a tutorial for calculating and visualizing historical global warming.

[![Binder](https://binder.pangeo.io/badge_logo.svg)](https://binder.pangeo.io/v2/gh/hdrake/cmip6-temperature-demo/master?filepath=notebooks%2F00_calculate_simulated_global_warming.ipynb)

Extending the analysis to projections of the future (out to 2100) is left as a guided exercise to the user, and solutions are provided in:

[![Binder](https://binder.pangeo.io/badge_logo.svg)](https://binder.pangeo.io/v2/gh/hdrake/cmip6-temperature-demo/master?filepath=notebooks%2F00s_solution_SSP_exercise.ipynb)


#### Calculating the Equilibrium Climate Sensitivity (ECS)

The following binder is a tutorial for calculating the Equilibrium Climate Sensitivity, i.e. the amount of warming at equilibrium due to a doubling to CO2, in the CMIP6 models, plotted as a probability histogram.


[![Binder](https://binder.pangeo.io/badge_logo.svg)](https://binder.pangeo.io/v2/gh/hdrake/cmip6-temperature-demo/master?filepath=notebooks%2F01_calculate_ECS.ipynb)

Note: in practice this example calculates the amount of warming due to a quadrupling of CO2, but conveniently this is equivalent to two doublings.
