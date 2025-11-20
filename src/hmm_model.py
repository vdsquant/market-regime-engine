import numpy as np
from hmmlearn.hmm import GaussianHMM

def fit_hmm(feature_series, n_states=3):
    """
    Fits a simple 1D HMM on a single series.
    Used ONLY in Day 1 to test pipeline.
    """
    X = feature_series.reshape(-1, 1)

    model = GaussianHMM(
        n_components=n_states,
        covariance_type="full",
        n_iter=300,
        random_state=42
    )

    model.fit(X)
    states = model.predict(X)

    return model, states
