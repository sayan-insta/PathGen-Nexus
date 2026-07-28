import json
from pathlib import Path

import pandas as pd

from src.logger.logger import logger

METADATA_DIR = Path("data/metadata")
METADATA_DIR.mkdir(parents=True, exist_ok=True)


class MetadataWriter:

    ###############################################################
    # PROJECT METADATA
    ###############################################################

    def save_projects(self, data):

        logger.info("Saving Project Metadata")

        json_path = METADATA_DIR / "projects.json"
        csv_path = METADATA_DIR / "projects.csv"

        with open(json_path, "w") as file:
            json.dump(data, file, indent=4)

        dataframe = pd.DataFrame(data["data"]["hits"])
        dataframe.to_csv(csv_path, index=False)

        logger.info("Projects Metadata Saved")

    ###############################################################
    # CASE METADATA
    ###############################################################

    def save_cases(self, data):

        logger.info("Saving Case Metadata")

        json_path = METADATA_DIR / "cases.json"
        csv_path = METADATA_DIR / "cases.csv"

        with open(json_path, "w") as file:
            json.dump(data, file, indent=4)

        dataframe = pd.DataFrame(data["data"]["hits"])
        dataframe.to_csv(csv_path, index=False)

        logger.info("Cases Metadata Saved")

    ###############################################################
    # FILE METADATA
    ###############################################################

    def save_files(self, data):

        logger.info("Saving File Metadata")

        json_path = METADATA_DIR / "files.json"
        csv_path = METADATA_DIR / "files.csv"

        with open(json_path, "w") as file:
            json.dump(data, file, indent=4)

        dataframe = pd.DataFrame(data["data"]["hits"])
        dataframe.to_csv(csv_path, index=False)

        logger.info("Files Metadata Saved")

    ###############################################################
    # RNA METADATA
    ###############################################################

    def save_rna(self, data):

        logger.info("Saving RNA Metadata")

        json_path = METADATA_DIR / "rna.json"
        csv_path = METADATA_DIR / "rna.csv"

        with open(json_path, "w") as file:
            json.dump(data, file, indent=4)

        dataframe = pd.DataFrame(data["data"]["hits"])
        dataframe.to_csv(csv_path, index=False)

        logger.info("RNA Metadata Saved")