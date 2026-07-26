from src.logger.logger import logger
from src.config.config import PROJECT_ROOT


def main():

    logger.info("Application Started")

    print("=" * 70)
    print("               PathGen-Nexus")
    print("=" * 70)

    print(f"\nProject Root:\n{PROJECT_ROOT}")

    logger.info("Project Root Printed")

    print("\nApplication Started Successfully")


if __name__ == "__main__":

    main()