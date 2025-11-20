import matplotlib.pyplot as plt

def plot_pca_loadings(components, maturities, title="Yield Curve PCA Loadings"):
    """
    Plots PCA loadings for each principal component across maturities.

    Parameters
    ----------
    components : np.ndarray
        PCA components matrix of shape (n_components, n_features).
        Each row corresponds to PC1, PC2, PC3...
    maturities : list or pd.Index
        Labels for x-axis (e.g., ['2Y', '5Y', '10Y']).
    title : str, optional
        Custom title for the plot.

    Notes
    -----
    - PCA loadings show how each maturity contributes to each component.
    - Interpretation for yield curves:
        * PC1 — Level (same sign across maturities)
        * PC2 — Slope (short vs long rates move opposite)
        * PC3 — Curvature (middle tenor bends differently)
    """

    plt.figure(figsize=(10, 6))

    for i, comp in enumerate(components):
        plt.plot(
            maturities,
            comp,
            marker='o',
            linewidth=2,
            label=f"PC{i+1}"
        )

    plt.title(title, fontsize=14)
    plt.xlabel("Maturity", fontsize=12)
    plt.ylabel("Loading Weight", fontsize=12)
    plt.grid(alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.show()
