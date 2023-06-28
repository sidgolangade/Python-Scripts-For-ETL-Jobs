# ETL Error Logging
This repository contains a Python script that demonstrates error handling and logging for an ETL (Extract, Transform, Load) process. The script showcases how to catch and handle exceptions during the ETL process and utilize the Python `logging` library to log important events, error messages, and statistics.

## Script Description
The script performs a simple ETL job and simulates an error by dividing a number by zero. It showcases the following features:

- Error handling: The script catches and handles exceptions during the ETL process using a `try-except` block.
- Logging: The `logging` library is used to log error messages and other relevant information during the ETL process.
- Informational messages: The script logs start and completion messages to indicate the progress of the ETL job.

## Prerequisites
- Python 3.x: Ensure you have Python 3.x installed on your system.
- Logging Library: The script uses the Python `logging` library.

## Usage
The script logs messages to the etl.log file. Open the file to view the log messages, including any error messages and completion status.
