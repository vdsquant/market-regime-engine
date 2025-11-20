from src.data_loader import load_yield_data, load_market_data
from src.pca_model import compute_pca_on_yields
from src.hmm_model import fit_hmm
from src.plots import plot_pca_loadings

import numpy as np

def main():
    print("Loading UK yield and market data...")
    yields = load_yield_data()
    market = load_market_data()

    print("Running PCA on UK gilt yields...")
    pca_results = compute_pca_on_yields(yields)
    print("Explained variance:", pca_results["explained_variance"])

    print("Plotting PCA loadings...")
    plot_pca_loadings(pca_results["components"], pca_results["input_columns"])

    print("Fitting HMM on FTSE returns (Day 1 test)...")
    returns = market["FTSE"].pct_change().dropna()   # FTSE replaces SPY
    model, states = fit_hmm(returns.values)          # simple 1D HMM

    print("Hidden states sample:", states[:20])

if __name__ == "__main__":
    main()
