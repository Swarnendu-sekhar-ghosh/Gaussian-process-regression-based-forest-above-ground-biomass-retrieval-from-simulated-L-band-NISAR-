# Hedwig

A Gaussian Process Regression model for estimating Forest Height (FH) and Above Ground Biomass (AGB) is proposed in this work. Backscatter intensities from 5 scenes (3 July,7 July,26 July,13 August and 1 october 2019) have been utilized as features to retrieve the forest height and above ground biomass. As it is a monostatic radar data utilizing the condition of asymmetry, we take the average of HV and VH intensity.

Step by step approach :

1. Modelling a GPR model utilizing a non-linear Matern-3/2 kernel to retrieve FH and AGB. This is performed for both full-pol information and dual-pol (HH+HV) information. Utilizing the lengthscale of the Matern-3/2 kernel as weights to check the importance of the backscatter intensities of each of the 5 dates.

2. The estimation of the forest height and the above ground biomass have been checked for different resolutions (20m,30,50mand 100m respectively).  

3. The results for the polarization infromation is then compared.

4. A 10-fold cross validation is utilized to check the performace of the model for the entire dataset. The mean and the standard deviation of RMSE and R^2 shows the accuracy of the GPR model for each scenario.

5. A temporal analysis of the backscatter intensities have been performed along with the soil-moisture and precipation during the considered periods to understand how the backscatter information vaires during the entire time period and does rain have any implications of the information that is retured to the radar.

6. Uncertainty results:

Forest height mean and uncertainty maps for known and complete area. 





