import logging
from app.db import wait_for_db

logger = logging.getLogger(__name__)

file_path = "analytics/analytics_queries.sql"
def run_analytic_queries(file_path,interactive=True):

    #wait for db connection
    connection = wait_for_db()
    
    if connection is None:
        logger.error("Failed to establish database connection")
        return None
    
    cursor = connection.cursor()
    
    #read sql queries from file
    with open(file_path, 'r') as sql_file:
        sql = sql_file.read()
        logger.info("Reading SQL file")
        
    queries = sql.split(";")

    #execute queries after removing unnescessary whitespace
    for query in queries:
        query = query.strip() 
        if not query:
             continue
        try:
            logger.info(f"Running query: {query}")
            cursor.execute(query)
        except Exception as e:
                logger.error(f"Could not execute the query:{query}")
                logger.error(f"Reason: Error - {e}")
                continue
    
        if cursor.description: # if query returned rows
                results = cursor.fetchall()
                for row in results:
                     logger.info(row)
        else:
             logger.info("Query Executed, returned No data")


    # Close Connection 
    connection.commit()
    cursor.close()
    connection.close()

    # Check if input query to be run
    if interactive:
        while True:
            choice = input(
            "1. Select 1 to enter a query\n"\
            "2. Select 2 to exit \n"\
            "Enter a choice: ")
            if choice == "1":
                run_analytic_queries_from_terminal()
            elif choice == "2":
                break;
            else:
                print("Incorrect selection")



def run_analytic_queries_from_terminal():

    #wait for db connection
    connection = wait_for_db()
    
    if connection is None:
        logger.error("Failed to establish database connection")
        return None
    
    cursor = connection.cursor()

    query_input = input("Enter the query to run: \n")
    query = query_input.strip()

    if not query:
        return
    try:
        logger.info(f"Running query from imput")
        cursor.execute(query)
    except Exception as e:
            logger.error(f"Could not execute the query:{query}")
            logger.error(f"Reason: Error - {e}")
            return

    if cursor.description: # if query returned rows
            results = cursor.fetchall()
            for row in results:
                    logger.info(row)
            logger.info("Query executed successfully !")
    else:
            logger.info("Query Executed, returned No data")

    connection.commit()
    cursor.close()
    connection.close()