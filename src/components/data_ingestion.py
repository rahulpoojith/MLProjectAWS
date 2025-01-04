import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', "train.csv")
    test_data_path: str = os.path.join('artifacts', "test.csv")
    raw_data_path: str = os.path.join('artifacts', "data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            # Verify the path to the file first
            file_path = 'notebook/data/stud.csv'  # Update with the correct relative or absolute path
            logging.info(f"Attempting to read file from: {file_path}")

            # Check if file exists
            if not os.path.exists(file_path):
                logging.error(f"File not found at {file_path}")
                raise FileNotFoundError(f"File not found: {file_path}")

            # Read the CSV file
            df = pd.read_csv(file_path)
            logging.info(f"File read successfully. Shape of data: {df.shape}")

            # Ensure the 'artifacts' directory exists
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            # Save raw data
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info("Raw data saved successfully")

            # Train-test split
            logging.info("Train-test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # Save train and test sets
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Data ingestion completed successfully")

            return self.ingestion_config.train_data_path, self.ingestion_config.test_data_path

        except Exception as e:
            logging.error(f"Error occurred: {str(e)}")
            raise CustomException(e, sys)

if __name__ == "__main__":
    obj = DataIngestion()
    try:
        train_data, test_data = obj.initiate_data_ingestion()
        logging.info(f"Train data saved at: {train_data}")
        logging.info(f"Test data saved at: {test_data}")
    except Exception as e:
        logging.error(f"Data ingestion failed: {str(e)}")
