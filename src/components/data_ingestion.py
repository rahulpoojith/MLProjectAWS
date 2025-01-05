import os
import sys
import pandas as pd
from dataclasses import dataclass
from sklearn.model_selection import train_test_split
from src.exception import CustomException
from src.logger import logging
from src.components.data_transformation import DataTransformationConfig, DataTransformation
from src.components.model_trainer import ModelTrainerConfig, ModelTrainer
from src.utils import save_object, evaluate_models


@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', "train.csv")
    test_data_path: str = os.path.join('artifacts', "test.csv")
    raw_data_path: str = os.path.join('artifacts', "data.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        """
        Handles data ingestion: Reads raw data, splits it into train and test sets, and saves them.
        """
        logging.info("Starting data ingestion process.")
        try:
            # Define the file path for raw data
            file_path = 'notebook/data/stud.csv'
            if not os.path.exists(file_path):
                logging.error(f"File not found: {file_path}")
                raise FileNotFoundError(f"File not found: {file_path}")

            # Load the dataset
            df = pd.read_csv(file_path)
            logging.info(f"Dataset loaded successfully with shape: {df.shape}")

            # Create the artifacts directory
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            # Save raw data
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            # Split the dataset into train and test sets
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Data ingestion completed successfully.")
            return self.ingestion_config.train_data_path, self.ingestion_config.test_data_path

        except Exception as e:
            logging.error(f"Error in data ingestion: {str(e)}")
            raise CustomException(e, sys)


if __name__ == "__main__":
    try:
        # Step 1: Data Ingestion
        data_ingestion = DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()
        logging.info(f"Data ingestion completed. Train data: {train_data_path}, Test data: {test_data_path}")

        # Step 2: Data Transformation
        data_transformation = DataTransformation()
        train_array, test_array, preprocessor_path = data_transformation.initiate_data_transformation(
            train_path=train_data_path, test_path=test_data_path
        )
        logging.info(f"Data transformation completed. Preprocessor saved at: {preprocessor_path}")

        # Step 3: Model Training
        model_trainer = ModelTrainer()
        r2_score = model_trainer.initiate_model_training(train_array=train_array, test_array=test_array)
        logging.info(f"Model training completed with R2 score: {r2_score}")

    except Exception as e:
        logging.error(f"Pipeline failed: {str(e)}")