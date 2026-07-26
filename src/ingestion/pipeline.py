"""
Data Ingestion Pipeline
"""

from src.ingestion.gdc_client import GDCClient
from src.ingestion.cases_client import CasesClient
from src.ingestion.metadata_writer import MetadataWriter
from src.logger.logger import logger


class DataIngestionPipeline:

    def __init__(self):

        self.project_client = GDCClient()
        self.case_client = CasesClient()
        self.writer = MetadataWriter()

    def run(self):

        logger.info("Pipeline Started")

        # Download project metadata
        projects = self.project_client.get_projects()
        self.writer.save_projects(projects)

        # Download TCGA-BRCA cases
        cases = self.case_client.get_cases()
        self.writer.save_cases(cases)

        logger.info("Pipeline Finished")

        print("\nTCGA-BRCA Cases Download Completed.")