import matplotlib.pyplot as plt

def plot_pca_loadings(components, maturities):
    plt.figure(figsize=(10, 5))
    for i, comp in enumerate(components):
        plt.plot(maturities, comp, marker='o', label=f"PC{i+1}")
    plt.legend()
    plt.title("Yield Curve PCA Loadings")
    plt.show()