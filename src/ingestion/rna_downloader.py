"""
Download RNA Expression Files
"""

from pathlib import Path

import pandas as pd
import requests

from src.logger.logger import logger


RNA_DOWNLOAD_DIR = Path("data/downloads/rna")
RNA_DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)


class RNADownloader:

    DOWNLOAD_URL = "https://api.gdc.cancer.gov/data/"

    def download(self):

        logger.info("Starting RNA File Download")

        dataframe = pd.read_csv("data/metadata/rna.csv")

        total_files = len(dataframe)

        logger.info(f"Found {total_files} RNA files")

        for index, row in dataframe.iterrows():

            file_id = row["file_id"]
            file_name = row["file_name"]

            output_file = RNA_DOWNLOAD_DIR / file_name

            # Skip if already downloaded
            if output_file.exists():

                logger.info(
                    f"[{index + 1}/{total_files}] Already exists: {file_name}"
                )

                continue

            logger.info(
                f"[{index + 1}/{total_files}] Downloading {file_name}"
            )

            response = requests.get(
                self.DOWNLOAD_URL + file_id,
                stream=True,
                timeout=300
            )

            response.raise_for_status()

            with open(output_file, "wb") as file:

                for chunk in response.iter_content(chunk_size=8192):

                    if chunk:

                        file.write(chunk)

        logger.info("RNA File Download Completed")