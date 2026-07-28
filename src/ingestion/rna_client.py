"""
Download RNA-Seq Metadata
"""

import requests

from src.logger.logger import logger


class RNAClient:

    URL = "https://api.gdc.cancer.gov/files"

    def get_rna_files(self):

        logger.info("Downloading RNA Metadata")

        filters = {
            "op": "and",
            "content": [

                {
                    "op": "=",
                    "content": {
                        "field": "cases.project.project_id",
                        "value": "TCGA-BRCA"
                    }
                },

                {
                    "op": "=",
                    "content": {
                        "field": "data_category",
                        "value": "Transcriptome Profiling"
                    }
                },

                {
                    "op": "=",
                    "content": {
                        "field": "data_type",
                        "value": "Gene Expression Quantification"
                    }
                }

            ]
        }

        fields = [
            "file_id",
            "file_name",
            "submitter_id",
            "data_type",
            "data_category",
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

        logger.info("RNA Metadata Downloaded")

        return response.json()