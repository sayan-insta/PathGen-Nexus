from pathlib import Path

import numpy as np
import pandas as pd

RESULTS_DIR = Path("results")
RESULTS_DIR.mkdir(exist_ok=True)

ORIGINAL = Path("data/processed/selected_features.csv")
LATENT = Path("data/processed/latent_features.csv")


class VAEEvaluation:

    def evaluate(self):

        original = pd.read_csv(ORIGINAL, index_col=0)
        latent = pd.read_csv(LATENT, index_col=0)

        compression_ratio = latent.shape[1] / original.shape[1]

        report = []

        report.append("===== VAE Evaluation =====")
        report.append("")
        report.append(f"Original Features : {original.shape[1]}")
        report.append(f"Latent Features   : {latent.shape[1]}")
        report.append(f"Samples           : {original.shape[0]}")
        report.append(f"Compression Ratio : {compression_ratio:.4f}")
        report.append(f"Reduction         : {(1-compression_ratio)*100:.2f}%")

        with open(RESULTS_DIR / "evaluation.txt", "w") as f:
            f.write("\n".join(report))

        print("\n".join(report))
        print("\nEvaluation report saved.")