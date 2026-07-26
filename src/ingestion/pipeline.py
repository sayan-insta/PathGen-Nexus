from src.ingestion.gdc_client import GDCClient
from src.ingestion.metadata_writer import MetadataWriter


class DataIngestionPipeline:

    def run(self):

        client = GDCClient()

        writer = MetadataWriter()

        data = client.get_projects()

        writer.save_projects(data)

        print("Metadata Download Completed")