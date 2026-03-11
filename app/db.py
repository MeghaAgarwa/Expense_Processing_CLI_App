import os
from dotenv import load_dotenv
import psycopg2
import time
import logging

logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()

def get_db_connection():
    connection = psycopg2.connect(
        host=os.getenv('POSTGRES_HOST'),
        port=os.getenv('POSTGRES_PORT'),
        database=os.getenv('POSTGRES_DB'),
        user=os.getenv('POSTGRES_USER'),
        password=os.getenv('POSTGRES_PASSWORD')
    )
    return connection

def wait_for_db():
    logger.info("Connecting to DB")
    attempts =0
    while attempts<=3:
        try:
            connection = get_db_connection()
            return connection
        except Exception as e:
            attempts+=1
            logger.info(f"DB connection error:{e}")
            logger.info(f"Retrying connection- Attempt number: {attempts}")
            time.sleep(5)

    