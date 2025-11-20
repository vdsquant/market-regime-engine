import numpy as np
from hmmlearn.hmm import GaussianHMM

def fit_hmm(feature_series, n_states=3):
    """
    Fits a Gaussian Hidden Markov Model (HMM) to a 1-dimensional feature series.

    Parameters
    ----------
    feature_series : np.ndarray
        1D array of numeric values (e.g., FTSE returns). Shape: (T,)
    n_states : int, optional
        Number of hidden regimes to estimate. Default is 3.

    Returns
    -------
    model : GaussianHMM
        Trained HMM model.
    states : np.ndarray
        Array of inferred hidden states for each time step. Shape: (T,)

    Notes
    -----
    - Day 1 uses a *single-feature HMM*, which is the simplest possible setup.
      This is ideal for validating the pipeline before adding multiple 
      macro/volatility/yield features in later versions.
    
    - The model assumes:
        * Gaussian emissions
        * Full covariance structure
        * 3 hidden regimes (Calm, Volatile, Stress) by default

    - This function can be extended later to:
        * Fit multi-dimensional HMMs
        * Use feature matrices instead of a single series
        * Add regime interpretation logic
        * Generate transition probability plots
    """

    # Ensure input shape is (T, 1)
    X = np.asarray(feature_series).reshape(-1, 1)

    # Define the HMM model
    model = GaussianHMM(
        n_components=n_states,
        covariance_type="full",
        n_iter=300,
        random_state=42,
        verbose=False
    )

    # Fit HMM to the data
    model.fit(X)

    # Predict hidden regime for each observation
    states = model.predict(X)

    return model, states
