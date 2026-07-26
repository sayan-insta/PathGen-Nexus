from src.ingestion.pipeline import DataIngestionPipeline
from src.logger.logger import logger


def main():

    logger.info("Starting Pipeline")

    pipeline = DataIngestionPipeline()

    pipeline.run()

    logger.info("Pipeline Finished")


if __name__ == "__main__":

    main()