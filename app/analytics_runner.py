import logging
from db import wait_for_db
from logger import setup_logger

logger = logger = setup_logger()

file_path = "analytics/analytics_queries.sql"
def run_analytic_queries(file_path):

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
