# Hedwig

An (Adaptive) Gaussian process regression model for estimating Forest Height (FH) and Above Ground Biomass (AGB). Backscatter intensities from 5 scenes (3 July,7 July,26 July,13 August and 1 october 2019) are available. Utilizing these backscatter intensities the GPR model will retrieve both the biophysical parameters. As it is a monostatic radar data utilizing the condition of asymmetry, we take the average of HV and VH intensity. the features considered are the backscatter intensitites of HH, (HV+VH/2) and VV from all the 5 scenes.

a) Primary approach :

Modelling a GPR model Utilizing a non-linear RBF kernel with a single lengthscale or a combination of linear and non-linear kernels to retrieve FH and AGB.

b) Secondary approach :

Utilizing the lengthscale of the RBF kernel as weights to check the importance of the backscatter intensities of each of the 5 dates. 

Uncertainty results:

Forest height mean and uncertainty maps for known and complete area. 





