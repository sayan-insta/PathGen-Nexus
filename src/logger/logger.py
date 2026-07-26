import logging

import os

from datetime import datetime

LOG_FOLDER = "logs"

os.makedirs(LOG_FOLDER, exist_ok=True)

LOG_FILE = datetime.now().strftime("%Y_%m_%d_%H_%M_%S.log")

LOG_PATH = os.path.join(LOG_FOLDER, LOG_FILE)

logging.basicConfig(

    filename=LOG_PATH,

    level=logging.INFO,

    format="[ %(asctime)s ] %(name)s %(levelname)s %(message)s"

)

logger = logging.getLogger("PathGen-Nexus")