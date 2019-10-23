# cmip6-temperature-demo

## A handful of tutorials for basic analysis of climate models from CMIP6 on the Google Cloud Platform

#### Analyzing state-of-the-art simulations of global warming (historical and future projections)

The following binder is a tutorial for calculating and visualizing historical global warming.

[![Binder](https://binder.pangeo.io/badge_logo.svg)](https://binder.pangeo.io/v2/gh/hdrake/cmip6-temperature-demo/master?filepath=notebooks%2F00_calculate_simulated_global_warming.ipynb)

Extending the analysis to projections of the future (out to 2100) is left as a guided exercise to the user, and solutions are provided in:

[![Binder](https://binder.pangeo.io/badge_logo.svg)](https://binder.pangeo.io/v2/gh/hdrake/cmip6-temperature-demo/master?filepath=notebooks%2F00s_solution_SSP_exercise.ipynb)


#### Calculating the Equilibrium Climate Sensitivity (ECS)

The following binder is a tutorial for calculating the Equilibrium Climate Sensitivity, i.e. the amount of warming at equilibrium (really, a few hundred years after doubling) due to a doubling to CO2, in the CMIP6 models, plotted as a probability histogram.

[![Binder](https://binder.pangeo.io/badge_logo.svg)](https://binder.pangeo.io/v2/gh/hdrake/cmip6-temperature-demo/master?filepath=notebooks%2F01_calculate_ECS.ipynb)

Note: the ECS estimated here are biased low (by a factor of 1.5-2) because the models have not yet equilibrated and most are only run for a ~150 years after quadrupling and have not yet reached equilibrium. Since model experiments are rarely run out for more than a few hundred years, the climate science community has apparently switched to the so-called “Gregory-method” for their estimates of ECS, which linear extrapolates the (non-linear) relationship between radiative imbalance at the top of atmosphere and the global mean surface air temperature (to extrapolate from 100-1000 years or so all the way out to equilibrium). The ECS is then defined as the zero-imbalance intercept temperature of the linear extrapolation. Apparently this is the method that has been used for most estimates of ECS you see since CMIP5. Although not in the standard Deck of CMIP experiments, some modelling centers have produced output from [long-term simulations that run 200+ years](http://www.longrunmip.org/). See [Angeline Pendergrass' repo](https://github.com/apendergrass/cmip6-ecs) for an application of the Gregory method which produces the large ECS estimates reported in the media.
