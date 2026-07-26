"""
Download TCGA-BRCA file metadata
"""

import requests

from src.logger.logger import logger


class FilesClient:

    URL = "https://api.gdc.cancer.gov/files"

    def get_files(self):

        logger.info("Downloading TCGA-BRCA File Metadata")

        filters = {
            "op": "and",
            "content": [
                {
                    "op": "=",
                    "content": {
                        "field": "cases.project.project_id",
                        "value": "TCGA-BRCA"
                    }
                }
            ]
        }

        fields = [
            "file_id",
            "file_name",
            "data_category",
            "data_type",
            "experimental_strategy",
            "cases.case_id",
            "cases.submitter_id"
        ]

        params = {
            "filters": str(filters).replace("'", '"'),
            "fields": ",".join(fields),
            "size": 2000,
            "format": "JSON"
        }

        response = requests.get(
            self.URL,
            params=params,
            timeout=120
        )

        response.raise_for_status()

        logger.info("File Metadata Downloaded")

        return response.json()