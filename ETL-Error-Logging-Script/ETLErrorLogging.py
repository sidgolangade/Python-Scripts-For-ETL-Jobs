import logging

def etl_job():
    try:
        # Perform ETL operations here
        # Simulate a failure by dividing by zero
        result = 10 / 0
    except Exception as e:
        # Handle the exception
        logging.error(f"An error occurred during the ETL process: {str(e)}")
        # Perform any necessary error handling or cleanup actions

# Configure logging
logging.basicConfig(filename='etl.log', level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

# Log an informational message
logging.info("Starting ETL job...")

# Call the ETL job function
etl_job()

# Log a success message
logging.info("ETL job completed successfully.")
