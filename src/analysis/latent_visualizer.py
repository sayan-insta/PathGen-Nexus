"""
Visualize Latent Features using PCA
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.decomposition import PCA

from src.logger.logger import logger


LATENT_PATH = Path("data/processed/latent_features.csv")

RESULTS_DIR = Path("results")

RESULTS_DIR.mkdir(
    parents=True,
    exist_ok=True
)


class LatentVisualizer:

    def visualize(self):

        logger.info("Loading Latent Features")

        df = pd.read_csv(
            LATENT_PATH,
            index_col=0
        )

        logger.info(
            f"Samples : {df.shape[0]}"
        )

        logger.info(
            f"Latent Dimensions : {df.shape[1]}"
        )

        pca = PCA(
            n_components=2,
            random_state=42
        )

        reduced = pca.fit_transform(df)

        reduced_df = pd.DataFrame(
            reduced,
            columns=["PC1", "PC2"],
            index=df.index
        )

        reduced_df.to_csv(
            RESULTS_DIR / "pca_latent.csv"
        )

        plt.figure(figsize=(8,6))

        plt.scatter(
            reduced_df["PC1"],
            reduced_df["PC2"],
            alpha=0.8
        )

        plt.xlabel("Principal Component 1")

        plt.ylabel("Principal Component 2")

        plt.title("VAE Latent Feature Visualization")

        plt.tight_layout()

        plt.savefig(
            RESULTS_DIR / "pca_plot.png",
            dpi=300
        )

        plt.close()

        logger.info("PCA Completed")

        print()
        print("=" * 60)
        print("Latent Feature Visualization Completed")
        print("=" * 60)
        print("CSV  : results/pca_latent.csv")
        print("Plot : results/pca_plot.png")