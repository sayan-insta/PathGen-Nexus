"""
Metadata Writer
"""

import json
import pandas as pd

from src.config.config import METADATA_DIR
from src.logger.logger import logger


class MetadataWriter:
    """
    Save API responses into JSON and CSV formats.
    """

    def __init__(self):

        METADATA_DIR.mkdir(parents=True, exist_ok=True)

    #####################################################################
    # PROJECT METADATA
    #####################################################################

    def save_projects(self, data):

        logger.info("Saving Project Metadata")

        json_path = METADATA_DIR / "projects.json"

        csv_path = METADATA_DIR / "projects.csv"

        with open(json_path, "w") as file:
            json.dump(data, file, indent=4)

        dataframe = pd.DataFrame(data["data"]["hits"])

        dataframe.to_csv(csv_path, index=False)

        logger.info("Project Metadata Saved Successfully")

    #####################################################################
    # CASE METADATA
    #####################################################################

    def save_cases(self, data):

        logger.info("Saving Case Metadata")

        json_path = METADATA_DIR / "cases.json"

        csv_path = METADATA_DIR / "cases.csv"

        with open(json_path, "w") as file:
            json.dump(data, file, indent=4)

        dataframe = pd.DataFrame(data["data"]["hits"])

        dataframe.to_csv(csv_path, index=False)

        logger.info("Case Metadata Saved Successfully")

    #####################################################################
    # FILE METADATA
    #####################################################################

    def save_files(self, data):

        logger.info("Saving File Metadata")

        json_path = METADATA_DIR / "files.json"

        csv_path = METADATA_DIR / "files.csv"

        with open(json_path, "w") as file:
            json.dump(data, file, indent=4)

        dataframe = pd.DataFrame(data["data"]["hits"])

        dataframe.to_csv(csv_path, index=False)

        logger.info("File Metadata Saved Successfully")