# R Programming Notes

## Advanced Data Structures

- A matrix can be thought of as a vector of vectors, where each value in the matrix is the same data type.


- A data frame is very similar to a Pandas DataFrame where each column can be a different data type.


- A tibble is a recent data object introduced by the tidyverse package in R and is an optimized data frame with extra metadata and features. The most current libraries and packages in R use data frames or tibbles; however, older R packages and analysis scripts will still use matrix objects to perform specific functions or analyses.

## Web Resources

<a href="https://cran.r-project.org/doc/manuals/r-release/R-intro.pdf" target="_blank">R-intro.pdf</a>

<a href="https://plotly.com/r/" target="_blank">Plotly R Open Source Graphics Library</a>

## Time Series Analysis

<a href="https://cran.r-project.org/web/packages/prophet/index.html" target="_blank">Prophet: Automatic Forecasting Procedure</a>

### Time Series functions
> #### ts(data, start, end, frequency)
>
> **data:** vector or matrix of continuous values
>
> **start:** starting time of first observation
>
> **end:** end time of last observation
>
> **frequency:** number of observations per unit of time
>
> **returns:** time series object


> #### diff(ts)
> 
> **ts**: time series object (data, lag, differences)
>
> **data:** time series object
>
> **lag:** lag at which to apply difference
>
> **differences:** order of differencing
>
> **returns:** a differencing time series 
> 
> <a href="https://atsa-es.github.io/atsa-labs/sec-tslab-differencing-to-remove-a-trend-or-seasonal-effects.html" target="_blank">Applied Time Series Analysis</a>






