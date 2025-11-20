import pandas as pd
from sklearn.decomposition import PCA

def compute_pca_on_yields(yields_df):
    """
    Computes PCA on daily changes of the yield curve.

    Parameters
    ----------
    yields_df : pd.DataFrame
        DataFrame of yield series or yield-curve proxies.
        Columns represent maturities (e.g., 2Y, 5Y, 10Y).
        Index is a DatetimeIndex.

    Returns
    -------
    dict
        {
            "pca": PCA object,
            "explained_variance": array of variance ratios,
            "components": PCA loadings matrix,
            "input_columns": column names,
            "diff_data": daily changes used for PCA
        }

    Notes
    -----
    - PCA should be applied to *changes* in yields rather than levels
      because levels are highly correlated, and PCA on levels tends 
      to artificially inflate PC1.

    - Typical UK yield curve dynamics:
        * PC1 — Level (parallel shifts)
        * PC2 — Slope (steepening/flattening)
        * PC3 — Curvature (butterfly movement)

    - Day 1 uses PCA only for feature extraction and visualisation.
      Later versions (Day 2+) will integrate PCs into multi-factor HMMs.
    """

    # 1. Compute daily changes — essential for proper PCA
    diff = yields_df.diff().dropna()

    # 2. Fit PCA with as many components as maturities
    n_components = len(diff.columns)
    pca = PCA(n_components=n_components)

    pca.fit(diff)

    return {
        "pca": pca,
        "explained_variance": pca.explained_variance_ratio_,
        "components": pca.components_,
        "input_columns": diff.columns,
        "diff_data": diff
    }
