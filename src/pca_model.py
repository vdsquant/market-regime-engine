import pandas as pd
from sklearn.decomposition import PCA

def compute_pca_on_yields(yields_df):
    # daily changes recommended for PCA on yield curve
    diff = yields_df.diff().dropna()

    pca = PCA(n_components=len(diff.columns))
    pca.fit(diff)

    return {
        "pca": pca,
        "explained_variance": pca.explained_variance_ratio_,
        "components": pca.components_,
        "input_columns": diff.columns
    }
