""" @file main.py
    @author Sean Duffie
    @brief The main of the project
"""
import sys
from loguru import logger
from project.config import settings
from project.logic import process_data

def setup_logging():
    # Remove the default handler (so you can configure your own)
    logger.remove()
    
    # Add a console handler (for you to see)
    logger.add(sys.stderr, level="INFO")
    
    # Add a file handler (for history)
    # "rotation" creates a new file every 10MB or every day
    # "retention" keeps logs for 10 days before deleting old ones
    logger.add("logs/app.log", rotation="10 MB", retention="10 days", level="DEBUG")

def main():
    setup_logging()
    logger.info(f"Connecting with key: {settings.api_key[:4]}****")

    try:
        # Your app logic here

        # Example of calling the logic
        final_output = process_data(10)
        print(f"The final result is: {final_output}")

        # result = 1 / 0
    except Exception:
        # Log the exception with a full stack trace automatically
        logger.exception("A critical error occurred")

if __name__ == "__main__":
    main()
