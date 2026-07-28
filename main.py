from src.ingestion.pipeline import DataIngestionPipeline
from src.logger.logger import logger


def main():

    logger.info("Starting Pipeline")

    pipeline = DataIngestionPipeline()

    pipeline.run()


if __name__ == "__main__":
    main()