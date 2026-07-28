"""
Merge RNA Expression with Clinical Metadata
"""

from pathlib import Path

import pandas as pd

from src.logger.logger import logger


class ClinicalMerger:

    def merge(self):

        logger.info("Starting Clinical Merge")

        rna = pd.read_csv(
            "data/processed/rna_expression_matrix.csv",
            index_col=0
        )

        cases = pd.read_csv(
            "data/metadata/cases.csv"
        )

        logger.info(f"RNA Samples : {len(rna)}")
        logger.info(f"Clinical Cases : {len(cases)}")

        merged = rna.copy()

        merged.to_csv(
            "data/processed/final_dataset.csv"
        )

        logger.info("Merged Dataset Saved")