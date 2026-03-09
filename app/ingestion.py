from datetime import date
import time
from venv import logger
from models.expense_model import Expense
from db import wait_for_db
from logger import setup_logger
import logging

logger = setup_logger(level=logging.INFO)

def insert_sample_expense(connection):

    #wait for db connection
    connection = wait_for_db()
    if connection is None:
        logger.error("Failed to establish database connection")
        return None
    cursor = connection.cursor()

    # Sample expense data
    title = "Lunch"
    expense_description = "Lunch with colleagues"
    amount = "15.50"
    category = "Food"
    expense_date = date(2024, 6, 1)
    
    # Insert sample expense into the database
    cursor.execute("""
        INSERT INTO expenses (title, expense_description, amount, category, expense_date)
        VALUES (%s, %s, %s, %s, %s)
    """, (title, expense_description, amount, category, expense_date))
    
    connection.commit()
    cursor.close()
    connection.close()


def ingest_CSV(records):

    #wait for db connection
    connection = wait_for_db()
    if connection is None:
        logger.error("Failed to establish database connection")
        return None
    cursor = connection.cursor()

     # Insert from the CSV files into the database

    for row in records:
        try:
            expense = Expense(**row)
            
            cursor.execute("""
                INSERT INTO expenses (title, expense_description, amount, category, expense_date)
                VALUES (%s, %s, %s, %s, %s)
            """, (expense.title, 
                  expense.expense_description, 
                  expense.amount, 
                  expense.category, 
                  expense.expense_date))
        except Exception as e:
            logger.error(f"Skipping invalid row:{row}")
            logger.error(f"Reason: Error - {e}")

    #logger.info("Custom Logger Working")
    
    connection.commit()
    cursor.close()
    connection.close()
    return expense
    

