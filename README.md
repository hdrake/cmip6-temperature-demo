# cmip6-temperature-demo


[![DOI](https://zenodo.org/badge/216607808.svg)](https://zenodo.org/badge/latestdoi/216607808)



## A handful of tutorials for basic analysis of climate models from CMIP6 on the Google Cloud Platform

#### Analyzing state-of-the-art simulations of global warming (historical and future projections)

The following binder is a tutorial for calculating and visualizing historical global warming.

[![Binder](https://binder.pangeo.io/badge_logo.svg)](https://binder.pangeo.io/v2/gh/hdrake/cmip6-temperature-demo/master?filepath=notebooks%2F00_calculate_simulated_global_warming.ipynb)

Extending the analysis to projections of the future (out to 2100) is left as a guided exercise to the user, and solutions are provided in:

[![Binder](https://binder.pangeo.io/badge_logo.svg)](https://binder.pangeo.io/v2/gh/hdrake/cmip6-temperature-demo/master?filepath=notebooks%2F00s_solution_SSP_exercise.ipynb)


#### Calculating the Equilibrium Climate Sensitivity (ECS)

The following binder is a tutorial for calculating the Equilibrium Climate Sensitivity, i.e. the amount of warming at equilibrium due to a doubling to CO2, in the CMIP6 models, plotted as a probability histogram and a bar plot.

[![Binder](https://binder.pangeo.io/badge_logo.svg)](https://binder.pangeo.io/v2/gh/hdrake/cmip6-temperature-demo/master?filepath=notebooks%2F01_calculate_ECS_Gregory_method.ipynb)

Note: the ECS estimated here using the Gregory method are biased low because of the linear extrapolation (see [Knutti and Rugenstein 2015](https://royalsocietypublishing.org/doi/full/10.1098/rsta.2015.0146)) but biased high by the use of a quadrupling (feedbacks are not constant!). Possibly more realistic results are obtained if the linear fit is calculated for later years, e.g. 20-150 or 100-150. See [Angeline Pendergrass' repo](https://github.com/apendergrass/cmip6-ecs) which does the same thing on the NCAR filesystem and includes several more models (also accounts for multiple realizations for each model).
