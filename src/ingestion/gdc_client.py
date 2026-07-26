"""
GDC API Client
"""

import requests

from src.logger.logger import logger

GDC_PROJECTS_URL = "https://api.gdc.cancer.gov/projects"


class GDCClient:

    def get_projects(self):

        logger.info("Requesting project list from GDC API")

        response = requests.get(GDC_PROJECTS_URL, timeout=30)

        response.raise_for_status()

        logger.info("Projects downloaded successfully")

        return response.json()