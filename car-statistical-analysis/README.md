## Project: Statistical Analysis with R

## Overview
Review manufacturing data on a new prototype vehicle called the `MechaCar` for AutosRUs (fictional car company).

- Perform multiple linear regression analysis to identify which variables in the dataset predict the mpg of MechaCar prototypes

- Collect summary statistics on the pounds per square inch (PSI) of the suspension coils from the manufacturing lots

- Run t-tests to determine if the manufacturing lots are statistically different from the mean population

- Design a statistical study to compare vehicle performance of the MechaCar vehicles against vehicles from other manufacturers.

- For each statistical analysis, write a summary interpretation of the findings.

## Linear Regression to predict MPG

<ins>Run from Terminal:</ins>

```bash
$ RScript MechaCarChallenge.RScript
```
<ins>Output:</ins>

```bash
Call:
lm(formula = mpg ~ vehicle_length + vehicle_weight + spoiler_angle +
    ground_clearance + AWD, data = mechaCar)

Residuals:
     Min       1Q   Median       3Q      Max
-19.4701  -4.4994  -0.0692   5.4433  18.5849

Coefficients:
                   Estimate Std. Error t value Pr(>|t|)
(Intercept)      -1.040e+02  1.585e+01  -6.559 5.08e-08 ***
vehicle_length    6.267e+00  6.553e-01   9.563 2.60e-12 ***
vehicle_weight    1.245e-03  6.890e-04   1.807   0.0776 .
spoiler_angle     6.877e-02  6.653e-02   1.034   0.3069
ground_clearance  3.546e+00  5.412e-01   6.551 5.21e-08 ***
AWD              -3.411e+00  2.535e+00  -1.346   0.1852
---
Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

Residual standard error: 8.774 on 44 degrees of freedom
Multiple R-squared:  0.7149,    Adjusted R-squared:  0.6825
F-statistic: 22.07 on 5 and 44 DF,  p-value: 5.35e-11
```

The r-squared value for the multiple linear regression model is 0.71 (71 %) which means that this model explains a significant amount of variability in the dependent variable, 71 % of the variability can be explained by the model.

We can conclude that the slope of this linear model does not equal zero because its r-squared value of 0.71 shows a moderate correlation between the linear model and the dependent variable MPG.

The y-intercept is statistically significant meaning it explains a significant amount of variability in MPG when all independent variables are zero.

The coefficients for `vehicle_length` and `ground_clearance` are statistically significant as they have p-values below the 0.05 threshold. The other coefficients for vehicle_weight, spoiler_angle, and AWD are not statistically significant in that their p-values are higher than 0.05.

## Summary Statistics on Suspension Coils

<ins>Run from Terminal:</ins>

```bash
$ RScript MechaCarChallenge.RScript
```
<ins>Output:</ins>

```bash
Mean Median Variance       SD
1 1498.78   1500 62.29356 7.892627
# A tibble: 3 x 5
# Groups:   Manufacturing_Lot [3]
  Manufacturing_Lot  Mean Median Variance     SD
  <chr>             <dbl>  <dbl>    <dbl>  <dbl>
1 Lot1              1500   1500     0.980  0.990
2 Lot2              1500.  1500     7.47   2.73
3 Lot3              1496.  1498.  170.    13.0
```

The overall variance (across all lots) of 62.29 is below the threshold of 100. However, the variance reported among the individual lots shows that Lot 3 has a lot of variability.

Lot 3 has a variance of 170 which exceeds the variance threshold of 100. So therefore, the current manufacturing data does not meet the variance specification in which the suspension coils must not exceed 100.

## T-Tests on Suspension Coils

<ins>One Sample t-test on PSI across all lots for mu=1500</ins>

```bash
One Sample t-test

data:  suspensionCoil$PSI
t = -1.8931, df = 149, p-value = 0.06028
alternative hypothesis: true mean is not equal to 1500
95 percent confidence interval:
1497.507 1500.053
sample estimates:
mean of x
1498.78
```

Based on the one sample t-test results above, we can conclude that the sample mean for the overall lots has a difference from the population mean due to randomness. The p-value of 0.06 means that we have to accept the null hypothesis that any differences between the sample mean and the population is due to randomness. The difference between the sample and population mean for PSI is not statistically significant.

<ins>One Sample t-test on PSI for each lot for mu=1500</ins>

```bash
        One Sample t-test Lot 1

data:  l1$PSI
t = 0, df = 49, p-value = 1
alternative hypothesis: true mean is not equal to 1500
95 percent confidence interval:
 1499.719 1500.281
sample estimates:
mean of x
     1500

        One Sample t-test Lot 2

data:  l2$PSI
t = 0.51745, df = 49, p-value = 0.6072
alternative hypothesis: true mean is not equal to 1500
95 percent confidence interval:
 1499.423 1500.977
sample estimates:
mean of x
   1500.2

        One Sample t-test Lot 3

data:  l3$PSI
t = -2.0916, df = 49, p-value = 0.04168
alternative hypothesis: true mean is not equal to 1500
95 percent confidence interval:
 1492.431 1499.849
sample estimates:
mean of x
  1496.14
```

The t-test for lot 3 indicates the difference between the sample and population mean is statistically significant and not due to randomness. This conclusion can be made because the p-value is less than 0.05.  The t-tests for lots 1 and 2 have p-values above 0.05 meaning that the null hypothesis is accepted. The differences in sample versus population means is due to randomness.

## Study Design: MechaCar vs Competition

The purpose of the experiment is to determine whether highway MPG is related to the price of a car among car make/models.

**Null Hypothesis** - The highway MPG is not related to the price of the car among different car models.

**Alternative Hypothesis** - The highway MPG of car models will determine the price of cars among different models.

1. Perform ANOVA test to determine if there are differences between the price and highway miles per gallon (MPG) among different car models

2. Create Boxplot to show the distribution of MPG for each car manufacturer

| Variable    | Values                                          |
|:------------|:------------------------------------------------|
| Price Range | $30,000 to $90,000                              |
| MPG         | Highway Miles Per Gallon (MPG)                  |
| Car Model   | Volkswagon, Acura, Lincoln, Audi, Buick, Honda  |

