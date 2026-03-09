import logging
import os
from dotenv import load_dotenv

def setup_logger(level=logging.INFO): # custom logger

    os.makedirs("logs", exist_ok=True)
    #get the level value from .env file
    load_dotenv()
    level = os.getenv("LOG_LEVEL", "INFO")

    logger = logging.getLogger(__name__)
    logger.setLevel(level)

    if not logger.handlers:

        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        # Adding console logging
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        #Adding file logging
        file_handler = logging.FileHandler('logs/log1.log')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger



