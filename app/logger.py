import logging
import os
from dotenv import load_dotenv

def setup_logger(level_default=logging.INFO): # custom logger

    os.makedirs("logs", exist_ok=True)
    #get the level value from .env file
    load_dotenv()
    level = os.getenv("LOG_LEVEL")
    if level is None:
        level = level_default

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG) 

    if not root_logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        # Adding console logging
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        console_handler.setFormatter(formatter)
        root_logger.addHandler(console_handler)

        #Adding file logging
        file_handler = logging.FileHandler('logs/log1.log')
        file_handler.setLevel(level)
        file_handler.setFormatter(formatter)
        root_logger.addHandler(file_handler)




