"""
Data Ingestion Pipeline
"""

from src.ingestion.gdc_client import GDCClient
from src.ingestion.cases_client import CasesClient
from src.ingestion.files_client import FilesClient
from src.ingestion.metadata_writer import MetadataWriter
from src.logger.logger import logger


class DataIngestionPipeline:
    """
    Executes the complete data ingestion pipeline.
    """

    def __init__(self):

        self.project_client = GDCClient()

        self.case_client = CasesClient()

        self.files_client = FilesClient()

        self.writer = MetadataWriter()

    def run(self):

        logger.info("=" * 80)
        logger.info("PATHGEN-NEXUS DATA INGESTION PIPELINE STARTED")
        logger.info("=" * 80)

        ###########################################################
        # STEP 1 : Download Project Metadata
        ###########################################################

        logger.info("Downloading Project Metadata...")

        projects = self.project_client.get_projects()

        self.writer.save_projects(projects)

        ###########################################################
        # STEP 2 : Download TCGA-BRCA Cases
        ###########################################################

        logger.info("Downloading TCGA-BRCA Cases...")

        cases = self.case_client.get_cases()

        self.writer.save_cases(cases)

        ###########################################################
        # STEP 3 : Download File Metadata
        ###########################################################

        logger.info("Downloading File Metadata...")

        files = self.files_client.get_files()

        self.writer.save_files(files)

        ###########################################################
        logger.info("=" * 80)
        logger.info("PIPELINE COMPLETED SUCCESSFULLY")
        logger.info("=" * 80)

        print("\n")
        print("=" * 60)
        print("PathGen-Nexus Pipeline Completed Successfully")
        print("=" * 60)