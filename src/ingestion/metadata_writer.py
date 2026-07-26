"""
Save metadata
"""

import json
import pandas as pd

from src.config.config import METADATA_DIR
from src.logger.logger import logger


class MetadataWriter:

    def save_projects(self, data):

        METADATA_DIR.mkdir(exist_ok=True)

        json_file = METADATA_DIR / "projects.json"

        csv_file = METADATA_DIR / "projects.csv"

        with open(json_file, "w") as file:

            json.dump(data, file, indent=4)

        logger.info("JSON saved")

        projects = data["data"]["hits"]

        df = pd.DataFrame(projects)

        df.to_csv(csv_file, index=False)

        logger.info("CSV saved")