import logging
import os
from datetime import datetime

# Generate log file name and path
log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_folder = os.path.join(os.getcwd(), "logs")
os.makedirs(log_folder, exist_ok=True)  # Ensure the logs folder exists

log_file_path = os.path.join(log_folder, log_file)

# Configure logging
logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s'
)

if __name__ == "__main__":
    logging.info("Logging has started")