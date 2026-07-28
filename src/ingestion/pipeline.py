from src.ingestion.gdc_client import GDCClient
from src.ingestion.cases_client import CasesClient
from src.ingestion.files_client import FilesClient
from src.ingestion.rna_client import RNAClient

from src.ingestion.rna_downloader import RNADownloader
from src.ingestion.metadata_writer import MetadataWriter

from src.logger.logger import logger


class DataIngestionPipeline:

    def __init__(self):

        self.gdc_client = GDCClient()
        self.case_client = CasesClient()
        self.file_client = FilesClient()
        self.rna_client = RNAClient()

        self.writer = MetadataWriter()

        self.rna_downloader = RNADownloader()

    def run(self):

        ############################################################
        # PROJECTS
        ############################################################

        logger.info("Downloading Projects...")

        projects = self.gdc_client.get_projects()

        self.writer.save_projects(projects)

        logger.info("Projects Completed")

        ############################################################
        # CASES
        ############################################################

        logger.info("Downloading Cases...")

        cases = self.case_client.get_cases()

        self.writer.save_cases(cases)

        logger.info("Cases Completed")

        ############################################################
        # FILES
        ############################################################

        logger.info("Downloading Files...")

        files = self.file_client.get_files()

        self.writer.save_files(files)

        logger.info("Files Completed")

        ############################################################
        # RNA METADATA
        ############################################################

        logger.info("Downloading RNA Metadata...")

        rna = self.rna_client.get_rna_files()

        self.writer.save_rna(rna)

        logger.info("RNA Metadata Completed")

        ############################################################
        # RNA FILE DOWNLOAD
        ############################################################

        logger.info("Downloading RNA Expression Files...")

        self.rna_downloader.download()

        logger.info("RNA Expression Files Download Completed")

        ############################################################
        # PIPELINE COMPLETED
        ############################################################

        print()
        print("=" * 65)
        print("PathGen-Nexus Pipeline Completed Successfully")
        print("=" * 65)