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
* **R Libraries**: `knitr`, `xtable`, `ggplot2`, `gridExtra`, `latex2exp`.

# Advanced Monte Carlo Integrations

This technical report demonstrates advanced Monte Carlo simulation techniques, focusing on multivariate probability distributions, complex geometric integrations, and variance reduction algorithms.

### Key Highlights:
* **Multivariate Normal Generation**: Implemented a custom generator for a 4D Normal distribution $N_4(\boldsymbol{\mu}, \Sigma)$ utilizing **Cholesky Decomposition** to preserve covariance structures.
* **Conditional & Generalized Ratio-of-Uniforms**: 
    * Sampled from a 2D density over a simplex using marginal/conditional density derivation and Inverse Transform Sampling.
    * Implemented the **Generalized Ratio-of-Uniforms ($r=3$)** method for a heavy-tailed 2D distribution, precisely calculating optimal bounding box limits.
* **Geometric Monte Carlo Integration**: Estimated the volume of an ellipsoid and the area of the **Mandelbrot set** using Crude Monte Carlo, tracking estimator convergence and asymptotic $1/\sqrt{n}$ confidence intervals.
* **Variance Reduction Techniques**: Systematically compared estimator efficiencies (Crude MC, **Antithetic Variates**, and **Importance Sampling**) for evaluating improper and highly oscillatory integrals, successfully minimizing standard errors under fixed computational budgets.

### Tools:
* **R Libraries**: `knitr`, `xtable`, `ggplot2`, `gridExtra`, `latex2exp`, `randtoolbox`, `pracma`, `ggExtra`, `grid`, `tidyr`, `dplyr`.

---

# CIFAR10 CNN Regularization

A Deep Learning experiment built with TensorFlow and Keras, focusing on the impact of different regularization and normalization techniques on Convolutional Neural Networks (CNNs) using the CIFAR-10 image dataset.

### Key Highlights:
* **CNN Architecture**: Designed a multi-layer Convolutional Neural Network for multi-class image classification.
* **Experimental Design**: Conducted a comparative analysis of three model variants:
    1. **Baseline Model**: Standard CNN architecture.
    2. **Batch Normalization**: Integrated BN layers to accelerate training and stabilize learning dynamics.
    3. **Dropout Regularization**: Applied Dropout layers to prevent network overfitting.
* **Performance Evaluation**: Visualized validation accuracy and validation loss trajectories using Matplotlib to assess the generalization capabilities of each technique.

### Tools:
* **Python**: `TensorFlow`, `Keras`, `Matplotlib`, `NumPy`.

# Connect4 AlphaBeta Agent

A highly optimized implementation of the Minimax algorithm for the Connect 4 game, engineered to play at a high level of difficulty (depth=7) with near-instant response times.

### Key Highlights & Algorithmic Optimizations:
* **Minimax with Alpha-Beta Pruning**: Implemented a recursive decision-making tree that trims unpromising branches, drastically reducing the search space.
* **In-Place State Mutation**: Avoided costly `deepcopy` operations by modifying and reverting the game board matrix in place, ensuring maximum simulation speed.
* **Local Win Detection**: Optimized terminal state checks by evaluating only the immediate vectors around the most recently dropped piece (rather than scanning the full board).
* **Heuristic Move Ordering**: Enforced center-to-edge column evaluation, forcing the Alpha-Beta algorithm to discover optimal paths earlier and maximize pruning efficiency.
* **Depth-Penalized Scoring**: Designed the heuristic engine to prioritize immediate wins over delayed wins, and delayed losses over immediate losses, ensuring natural and strategic gameplay.

### Tools:
* **Python**: `math`, `copy`.
