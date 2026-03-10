from datetime import date
from app.models.expense_model import Expense
from app.db import wait_for_db
from app.logger import setup_logger

logger = setup_logger()

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
    

