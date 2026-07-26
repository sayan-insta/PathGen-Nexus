"""
Download TCGA-BRCA Cases
"""

import requests

from src.logger.logger import logger


class CasesClient:
    """
    Client for downloading TCGA-BRCA case metadata.
    """

    URL = "https://api.gdc.cancer.gov/cases"

    def __init__(self):
        self.url = self.URL

    def get_cases(self):
        """
        Download TCGA-BRCA case metadata
        """

        logger.info("Downloading TCGA-BRCA Cases")

        filters = {
            "op": "=",
            "content": {
                "field": "project.project_id",
                "value": "TCGA-BRCA"
            }
        }

        params = {
            "filters": str(filters).replace("'", '"'),
            "size": 1000,
            "format": "JSON"
        }

        response = requests.get(
            self.url,
            params=params,
            timeout=60
        )

        response.raise_for_status()

        logger.info("TCGA-BRCA Cases Downloaded Successfully")

        return response.json()