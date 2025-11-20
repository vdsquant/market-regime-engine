Market Regime Engine (UK Edition)

A modular Python project that detects market regimes using:

PCA on UK gilt ETF proxies (yield curve movements)
Hidden Markov Models (HMM) on FTSE 100 returns
Clean feature engineering and plotting utilities
Production-ready folder structure (src/ modules)

This is Day 1 of a multi-stage build that will evolve into a complete market-regime detection engine.

Features (Day 1 MVP)
UK Gilt Yield Curve Processing
Uses UK gilt ETF proxies from Yahoo Finance:
IGLS → Short-term (proxy for 2Y)
IGLT → Medium term (proxy for 5Y)
GLTL → Long term (proxy for 10Y)

Daily close prices converted into a yield-curve feature matrix
PCA applied to extract:
PC1 — Level
PC2 — Slope
PC3 — Curvature

FTSE 100 Data Loader

Fetches FTSE (^FTSE) price history
Computes daily returns

Hidden Markov Model (HMM)
Gaussian HMM with 3 states
Fitted on FTSE returns
Outputs hidden state sequence (regimes)

Visualisations
PCA loading plots
Yield curve component behavior

Project Structure

market-regime-engine/
│
├── src/
│   ├── data_loader.py      # Fetches UK gilt ETFs + FTSE index
│   ├── pca_model.py        # PCA model for yield curve factors
│   ├── hmm_model.py        # Hidden Markov Model implementation
│   ├── plots.py            # PCA loading plots
│   └── __init__.py
│
├── main.py                 # Day 1 pipeline runner
├── requirements.txt         # Python dependencies
├── .gitignore               # venv + cache ignored
└── README.md                # You are here

Installation
1. Clone the repository
git clone https://github.com/vdsquant/market-regime-engine.git
cd market-regime-engine

2. Create a Python environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

3. Install dependencies
pip install -r requirements.txt

Run the Project
python main.py

This executes the Day-1 pipeline:

Load UK gilt ETFs
Run PCA
Plot PCA loadings
Load FTSE returns
Fit HMM
Print first 20 hidden states

Example Output
PCA Explained Variance
Indicates how much of the yield curve movement each principal component explains.

Hidden States Sample
[2 2 2 2 1 1 0 0 0 1 2 2 ... ]

Represents market regimes such as:
0 → Calm
1 → Volatile
2 → Stress

(Exact interpretation requires Day 2+ features.)

Roadmap (Next Steps)
Day 2 — Feature Expansion
Add volatility indices (VIX, UKVOL)
Add macro indicators (inflation, unemployment, PMI)
Add yield curve slope: 10Y–2Y
Combine all into multi-dimensional HMM

Day 3 — Regime Visualisation
FTSE chart coloured by hidden regime
Transition matrix + stationary probabilities

Day 4 — Backtesting
Strategy rules per regime
Performance metrics: Sharpe, drawdown

Day 5 — Package & API
Convert project into pip-installable package
Create CLI commands
Add Docker support

Why This Project Matters

Market regime detection is used by:
Quant hedge funds
Asset managers
Risk management teams
Macro researchers

This project demonstrates:
Structured engineering
Feature extraction
Time-series modelling
PCA + HMM workflow
Clean reproducible code

This repo will expand significantly over time.
Pull requests and ideas are welcome.

License
MIT License — free to use and modify.