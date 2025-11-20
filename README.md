
# Market Regime Engine (UK Edition)

## Overview
The **Market Regime Engine (UK Edition)** is a modular quantitative research project designed to detect latent market regimes in UK financial markets.  
The system integrates:
- **Principal Component Analysis (PCA)** on UK gilt ETF proxies to extract yield-curve factors  
- **Gaussian Hidden Markov Models (HMMs)** on FTSE 100 returns to infer hidden regimes  
- A clean, extensible `src/` architecture for future model expansion  

This project represents **Day 1** of a multi-stage build that will evolve into a full-featured market regime research and backtesting framework.

---

## Research Motivation
Financial markets often operate under **unobservable regimes** (e.g., calm, volatile, stressed). Detecting these states enhances:
- risk management  
- allocation decisions  
- asset-pricing insights  
- macro-financial interpretation  

The PCA + HMM approach follows established literature (Hamilton, 1989; Ang & Piazzesi, 2003; Guidolin & Timmermann, 2007) and provides a robust foundation for empirical regime-switching analysis.

---

## Data Sources

### Yield Curve Proxies (UK ETFs)
Due to limited long-term availability of actual UK gilt yield curve data, the project uses liquid bond ETFs as proxies:

| ETF  | Proxy for | Approx Tenor |
|------|-----------|--------------|
| IGLS | Short end | 2Y |
| IGLT | Mid curve | 5Y |
| GLTL | Long end | 10Y |

Daily close prices are differenced to obtain yield-curve innovations used in PCA.

### Equity Index
- **FTSE 100 Index (^FTSE)**  
Daily returns form the observation series for the Day‑1 HMM.

---

## Methodology

### 1. Principal Component Analysis (PCA)
PCA is applied to **daily yield-curve changes** rather than levels to avoid artificial correlation dominance.  
Interpretable factors typically emerge:

1. **PC1 — Level**  
2. **PC2 — Slope**  
3. **PC3 — Curvature**

These factors summarise most systematic movements of the gilt curve.

---

### 2. Hidden Markov Model (HMM)
A 1‑dimensional Gaussian HMM is fitted to FTSE returns:

\[
r_t \sim \mathcal{N}(\mu_{s_t}, \sigma_{s_t}^2), \quad s_t \in \{0,1,2\}
\]

Outputs include:
- filtered regime sequence  
- volatility characteristics by regime  
- transition dynamics (in later days)

Day 1 focuses only on core inference.

---

## Project Structure

```
market-regime-engine/
│
├── src/
│   ├── data_loader.py       # UK ETFs + FTSE loader
│   ├── pca_model.py         # PCA extraction
│   ├── hmm_model.py         # Gaussian HMM
│   ├── plots.py             # PCA loading plots
│   └── __init__.py
│
├── main.py                  # Day‑1 pipeline
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Installation

### Clone repository
```bash
git clone https://github.com/vdsquant/market-regime-engine.git
cd market-regime-engine
```

### Create environment
```bash
python -m venv venv
venv\Scripts\activate     # Windows  
source venv/bin/activate    # macOS/Linux
```

### Install dependencies
```bash
pip install -r requirements.txt
```

---

## Running the Day‑1 Pipeline

```bash
python main.py
```

Pipeline steps:
1. Download UK gilt ETF data and FTSE index  
2. Compute PCA on gilt-curve innovations  
3. Plot PCA loadings  
4. Compute FTSE returns  
5. Fit a 3‑state Gaussian HMM  
6. Print initial regime sequence  

---

## Example Output (Conceptual)

### PCA Explained Variance
Usually dominated by PC1 reflecting broad level shifts.

### Sample HMM States
```
[2 2 2 1 1 0 0 0 1 2 ...]
```

Interpretation (to be refined in Day 2+):
- **0 — Calm**
- **1 — Medium Volatility**
- **2 — Stress**

---

## Roadmap

### Day 2 — Multi-factor Input
- Add FTSE volatility  
- Add macro factors (CPI, PMI, unemployment)  
- Construct multi‑dimensional HMM input  

### Day 3 — Regime Visualisation
- Regime‑coloured FTSE chart  
- Transition matrices & stationary probabilities  

### Day 4 — Backtesting
- Regime‑based asset allocation rules  
- Sharpe, drawdown, turnover metrics  

### Day 5 — Packaging
- Publish as Python package  
- Add command‑line interface  
- Add Docker container  

---

## Academic Relevance
This project follows frameworks used in empirical macro‑finance and term‑structure modelling literature.  
It provides an open‑source foundation for:

- yield‑curve modelling  
- regime‑switching analytics  
- systematic trading research  
- risk‑state identification  

---

## License
MIT License. Free for research, academic, and commercial use.

