"""
Feature Selection using Variance Threshold
"""

from pathlib import Path

import pandas as pd

from src.logger.logger import logger


INPUT = Path("data/processed/final_dataset.csv")
OUTPUT = Path("data/processed/selected_features.csv")


class FeatureSelector:

    def select(self, top_n=5000):

        logger.info("Starting Feature Selection")

        df = pd.read_csv(INPUT, index_col=0)

        variances = df.var(axis=0)

        top_genes = variances.sort_values(
            ascending=False
        ).head(top_n).index

        selected = df[top_genes]

        selected.to_csv(OUTPUT)

        logger.info(
            f"Selected {selected.shape[1]} genes"
        )

        logger.info(
            f"Saved : {OUTPUT}"
        )

        print()
        print("=" * 60)
        print("Feature Selection Completed")
        print(f"Samples : {selected.shape[0]}")
        print(f"Genes : {selected.shape[1]}")
        print("=" * 60)