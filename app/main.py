
from ingestion import ingest_CSV
from multiple_csv_reader import read_CSV_from_Folder
from analytics_runner import run_analytic_queries
import sys
from logger import setup_logger

logger = setup_logger()

file_path = "analytics/analytics_queries.sql"
csv_folder = "data"         # for reading multiple csv files

def main():
    if len(sys.argv)== 1: #ingest_CSV
        logger.info("Starting CSV Ingestion")
        csv_folder = "data" 
        records= read_CSV_from_Folder(csv_folder)
        new_expense =ingest_CSV(records)
        logger.info(f"Expense inserted successfully:{new_expense}")
        logger.info("Ingestion Complete")

    elif len(sys.argv) >= 2:
        command = sys.argv[1]
        match command:
            case "analytics":
                logger.info("Running analytics")
                run_analytic_queries(file_path)
                logger.info("Analytics complete")
            case _:
                print("Try again with correct Command: analytics")
                logger.info("Invalid CLI command")
    else:
        logger.info("no command recieved")
    

if __name__ == "__main__":
    main()