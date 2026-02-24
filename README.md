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
