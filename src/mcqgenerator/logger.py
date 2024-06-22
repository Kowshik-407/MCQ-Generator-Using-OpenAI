# Import all the necessary packages
import logging
import os
from datetime import datetime

# Creating a log file at particular timestamp
LOG_FILE = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"

# Storing the logfile
log_path = os.path.join(os.getcwd(), "logs") # Logfile is logged into the current working directory + /logs
os.makedirs(log_path, exist_ok=True) # Then, creating the directory to the log_path

# File Path of the LogFile
LOG_FILEPATH = os.path.join(log_path, LOG_FILE)

# Finally, logging the data
logging.basicConfig(
  level=logging.INFO,
  filename=LOG_FILEPATH,
  format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)