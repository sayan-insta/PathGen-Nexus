"""
RNA Expression Preprocessor
"""

from pathlib import Path

import pandas as pd

from src.logger.logger import logger


RNA_DIR = Path("data/downloads/rna")
OUTPUT_DIR = Path("data/processed")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


class RNAPreprocessor:

    def process(self):

        logger.info("Starting RNA preprocessing")

        files = sorted(RNA_DIR.glob("*.tsv"))

        if len(files) == 0:
            logger.warning("No RNA files found")
            return

        expression_matrix = []

        sample_names = []

        gene_names = None

        for file in files:

            dataframe = pd.read_csv(
                file,
                sep="\t",
                comment="#"
            )

            dataframe = dataframe[
                dataframe["gene_type"] == "protein_coding"
            ]

            if gene_names is None:
                gene_names = dataframe["gene_name"].tolist()

            expression_matrix.append(
                dataframe["tpm_unstranded"].values
            )

            sample_names.append(file.stem)

        matrix = pd.DataFrame(
            expression_matrix,
            columns=gene_names,
            index=sample_names
        )

        output_file = OUTPUT_DIR / "rna_expression_matrix.csv"

        matrix.to_csv(output_file)

        logger.info(
            f"RNA Matrix Saved : {output_file}"
        )

        logger.info(
            f"Samples : {matrix.shape[0]}"
        )

        logger.info(
            f"Genes : {matrix.shape[1]}"
        )