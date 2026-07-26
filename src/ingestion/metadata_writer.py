"""
Metadata Writer
"""

import json

import pandas as pd

from src.config.config import METADATA_DIR
from src.logger.logger import logger


class MetadataWriter:
    """
    Save API responses as JSON and CSV.
    """

    def __init__(self):

        METADATA_DIR.mkdir(parents=True, exist_ok=True)

    ####################################################################
    # PROJECT METADATA
    ####################################################################

    def save_projects(self, data):

        json_path = METADATA_DIR / "projects.json"

        csv_path = METADATA_DIR / "projects.csv"

        with open(json_path, "w") as file:
            json.dump(data, file, indent=4)

        logger.info("Project JSON Saved")

        dataframe = pd.DataFrame(data["data"]["hits"])

        dataframe.to_csv(csv_path, index=False)

        logger.info("Project CSV Saved")

    ####################################################################
    # CASE METADATA
    ####################################################################

    def save_cases(self, data):

        json_path = METADATA_DIR / "cases.json"

        csv_path = METADATA_DIR / "cases.csv"

        with open(json_path, "w") as file:
            json.dump(data, file, indent=4)

        logger.info("Cases JSON Saved")

        dataframe = pd.DataFrame(data["data"]["hits"])

        dataframe.to_csv(csv_path, index=False)

        logger.info("Cases CSV Saved")