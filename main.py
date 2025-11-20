from src.data_loader import load_yield_data, load_market_data
from src.pca_model import compute_pca_on_yields
from src.hmm_model import fit_hmm
from src.plots import plot_pca_loadings

import numpy as np


def main():
    """
    Day 1 Pipeline:
    ---------------
    1. Load UK gilt ETF proxies and FTSE index
    2. Compute PCA on gilt curve (daily changes)
    3. Plot PCA loadings for interpretation
    4. Fit a simple 1D Gaussian HMM on FTSE returns
    5. Print sample hidden state sequence

    Notes:
    - This is a minimal MVP pipeline for validating that all modules work
      together (data loader → PCA → plotting → HMM).
    - Day 2+ will extend this to multi-feature HMMs and backtesting.
    """

    print("===============================================")
    print("      UK Market Regime Engine – Day 1")
    print("===============================================")

    # -------------------------------------------------
    # Load data
    # -------------------------------------------------
    print("\nLoading UK yield and market data...")
    yields = load_yield_data()
    market = load_market_data()

    print(f"Loaded yields with shape {yields.shape}")
    print(f"Loaded FTSE data with shape {market.shape}")

    # -------------------------------------------------
    # PCA on UK gilt curve
    # -------------------------------------------------
    print("\nRunning PCA on UK gilt yields...")
    pca_results = compute_pca_on_yields(yields)

    print("\nExplained Variance Ratio (PC1, PC2, PC3):")
    print(pca_results["explained_variance"])

    # -------------------------------------------------
    # PCA Loadings plot
    # -------------------------------------------------
    print("\nPlotting PCA loadings...")
    plot_pca_loadings(
        pca_results["components"], 
        pca_results["input_columns"],
        title="UK Gilt Curve – PCA Loadings"
    )

    # -------------------------------------------------
    # Fit simple 1D HMM on FTSE returns
    # -------------------------------------------------
    print("\nFitting HMM on FTSE 100 returns (Day 1 test)...")
    returns = market["FTSE"].pct_change().dropna()

    model, states = fit_hmm(returns.values)

    print("\nHidden states (first 20):")
    print(states[:20])

    print("\nDay 1 pipeline completed successfully.")


if __name__ == "__main__":
    main()
