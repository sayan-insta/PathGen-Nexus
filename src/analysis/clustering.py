from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score, davies_bouldin_score

RESULTS_DIR = Path("results")
RESULTS_DIR.mkdir(exist_ok=True)

LATENT_PATH = Path("data/processed/latent_features.csv")


class LatentClustering:

    def cluster(self):

        print("Loading latent features...")

        df = pd.read_csv(
            LATENT_PATH,
            index_col=0
        )

        kmeans = KMeans(
            n_clusters=3,
            random_state=42,
            n_init=10
        )

        labels = kmeans.fit_predict(df)

        sil = silhouette_score(df, labels)

        db = davies_bouldin_score(df, labels)

        print(f"Silhouette Score      : {sil:.4f}")
        print(f"Davies-Bouldin Score  : {db:.4f}")

        cluster_df = df.copy()

        cluster_df["Cluster"] = labels

        cluster_df.to_csv(
            RESULTS_DIR / "clusters.csv"
        )

        pca = PCA(
            n_components=2,
            random_state=42
        )

        reduced = pca.fit_transform(df)

        plt.figure(figsize=(8,6))

        plt.scatter(
            reduced[:,0],
            reduced[:,1],
            c=labels
        )

        plt.xlabel("PC1")

        plt.ylabel("PC2")

        plt.title("Latent Feature Clusters")

        plt.tight_layout()

        plt.savefig(
            RESULTS_DIR / "cluster_plot.png",
            dpi=300
        )

        plt.close()

        print("\nCluster plot saved.")