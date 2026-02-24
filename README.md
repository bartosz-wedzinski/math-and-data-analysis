# Time Series Forecasting Analysis

A comprehensive time series study comparing classical and modern forecasting techniques using the `euretail` dataset.

### Technical Highlights:
* **Exploratory Data Analysis**: Stationarity testing (ADF, KPSS) and seasonal decomposition.
* **Feature Engineering**: Variance stabilization via **Box-Cox transformation** and seasonal/regular differencing.
* **Advanced Modeling**:
    * **SARIMA**: Manual and automated identification of seasonal ARIMA orders.
    * **ETS**: Error-Trend-Seasonal state-space models with damped trend support.
    * **Decomposition**: Comparison of Classical vs. **STL (Loess-based)** decomposition.
* **Performance Evaluation**: Model ranking based on AICc/BIC and out-of-sample accuracy metrics (RMSE, MAE, MAPE, MASE).
* **Critical Thinking**: Included analysis of structural breaks (2008 crisis) and their impact on automated parameter selection.

### Tools:
* **R Libraries**: `forecast`, `fpp2`, `tseries`, `ggplot2`, `kableExtra`, `knitr`, `gridExtra`, `dplyr`, `tidyr`, `nortest`.

# Global Temperature Time Series: Detrending vs. Differencing

An in-depth autoregressive (AR) modeling project analyzing global temperature anomalies (1850-2023), focusing on the methodological differences between stochastic and deterministic trend removal.

### Key Highlights:
* **Stationarity Transformations**: Contrasted **first-order differencing** (stochastic approach) against **5th-degree polynomial detrending** (deterministic approach) to stabilize the mean.
* **AR(p) Modeling**: Automated order selection utilizing **AIC** and **FPE** criteria, followed by parameter estimation comparing **Yule-Walker** equations and **Maximum Likelihood Estimation (MLE)**.
* **Rigorous Diagnostics**: Validated model residuals using Ljung-Box tests, ACF visualizations (white noise evaluation), Shapiro-Wilk, and Jarque-Bera tests.
* **Forecasting & Critical Analysis**: Generated 10-year inverse-transformed forecasts. Included a critical evaluation of prediction intervals, highlighting the "funnel of uncertainty" in differenced models versus the overconfident "tunnel" effect and overfitting risks associated with high-degree polynomial detrending.

### Tools:
* **R Libraries**: `astsa`, `forecast`, `tseries`, `ggplot2`, `gridExtra`, `knitr`, `kableExtra`, `dplyr`, `tidyr`, `nortest`.

# Monte Carlo RNG Algorithms

This project focuses on the algorithmic implementation and mathematical derivation of random number generators (RNG) for various probability distributions, built entirely from scratch using only the standard uniform distribution (`runif`).

### Key Highlights:
* **Discrete Distributions**: Custom implementation of Bernoulli, Binomial, and Poisson generators using cumulative probability thresholds.
* **Continuous Distributions (Inverse Transform Sampling)**: Mathematical derivation of the inverse CDF for the **Weibull** distribution and implementation for Exponential and Laplace distributions.
* **Box-Muller Transform**: Bivariate normal distribution generation. Included empirical proof and joint-distribution visualizations to demonstrate the statistical independence of the generated variables.
* **Acceptance-Rejection Method**: Designed a custom Normal distribution generator using Laplace as the majorizing function. Solved the calculus optimization problem to find the exact parameters ($M$ and $\lambda$) that minimize the rejection rate.
* **Performance Benchmarking**: Comparative execution time analysis between the Box-Muller transform and the Acceptance-Rejection method.

### Tools:
* **R Libraries**: `knitr`, `xtabke`, `ggplot2`, `gridExtra`, `latex2exp` for mathematical data visualization.
