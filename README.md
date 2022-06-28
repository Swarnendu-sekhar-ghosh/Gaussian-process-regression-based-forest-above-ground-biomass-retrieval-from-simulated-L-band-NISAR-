# Hedwig

An  Gaussian process regression model for estimating Forest Height (FH) and Above Ground Biomass (AGB). Backscatter intensities from 5 scenes (3 July,7 July,26 July,13 August and 1 october 2019) are available. Utilizing these backscatter intensities the GPR model will retrieve both the biophysical parameters. As it is a monostatic radar data utilizing the condition of asymmetry, we take the average of HV and VH intensity. the features considered are the backscatter intensitites of HH, (HV+VH/2) and VV from all the 5 scenes.

Step by step approach :

1. Modelling a GPR model Utilizing a non-linear Matern-3/2 kernel to retrieve FH and AGB. This is performed for both full-pol information and Dual-pol information. Utilizing the lengthscale of the Matern-3/2 kernel as weights to check the importance of the backscatter intensities of each of the 5 dates. 
The results for the polarization infromation is then compared.

A 10 fold cross validation is utilized to check the performace of the model for the entire dataset. The mean and the standard deviation of RMSE and R^2 shows the accuracy of the GPR model for each scenario.



Uncertainty results:

Forest height mean and uncertainty maps for known and complete area. 





