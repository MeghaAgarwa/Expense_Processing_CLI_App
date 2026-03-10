from app.ingestion import ingest_CSV
from app.multiple_csv_reader import read_CSV_from_Folder
from app.analytics_runner import run_analytic_queries
import sys
import subprocess
from app.logger import setup_logger

logger = setup_logger()

file_path = "analytics/analytics_queries.sql"
csv_folder = "data"         # for reading multiple csv files

def main():
    # if len(sys.argv)== 1: #ingest_CSV
    #     logger.info("Starting CSV Ingestion")
    #     csv_folder = "data" 
    #     records= read_CSV_from_Folder(csv_folder)
    #     new_expense =ingest_CSV(records)
    #     logger.info(f"Expense inserted successfully:{new_expense}")
    #     logger.info("Ingestion Complete")

    if len(sys.argv) >= 2: # run analytics 
        command = sys.argv[1]
        match command:
            case "-ingest":
                logger.info("Starting CSV Ingestion")
                csv_folder = "data" 
                records= read_CSV_from_Folder(csv_folder)
                new_expense =ingest_CSV(records)
                logger.info(f"Expense inserted successfully:{new_expense}")
                logger.info("Ingestion Complete")

            case "-analytics":
                logger.info("Running analytics")
                run_analytic_queries(file_path)
                logger.info("Analytics complete")

            case "-tests":
                logger.info("Running tests")
                subprocess.run("pytest")
            case _:
                print("Try again with correct Command: analytics")
                logger.info("Invalid CLI command")
    else:
        logger.info("No command recieved: Try -ingest or -analytics or -tests" )
    

if __name__ == "__main__":
    main()