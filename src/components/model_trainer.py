import os
import sys
from dataclasses import dataclass
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, AdaBoostRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from xgboost import XGBRegressor
from catboost import CatBoostRegressor
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object, evaluate_models


@dataclass
class ModelTrainerConfig:
    trained_model_file_path: str = os.path.join('artifacts', "model.pkl")


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_training(self, train_array, test_array):
        """
        Trains and evaluates multiple regression models, saving the best-performing model.
        """
        try:
            logging.info("Splitting the data into training and test sets.")
            X_train, y_train, X_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1],
            )

            # Log data shapes for verification
            logging.info(f"Shapes - X_train: {X_train.shape}, y_train: {y_train.shape}, "
                         f"X_test: {X_test.shape}, y_test: {y_test.shape}")

            # Define models to train
            models = {
                "LinearRegression": LinearRegression(),
                "RandomForestRegressor": RandomForestRegressor(),
                "GradientBoostingRegressor": GradientBoostingRegressor(),
                "AdaBoostRegressor": AdaBoostRegressor(),
                "XGBRegressor": XGBRegressor(),
                "CatBoostRegressor": CatBoostRegressor()
            }

            logging.info("Evaluating models...")
            model_report = evaluate_models(X_train, y_train, X_test, y_test, models)

            if not model_report:
                raise CustomException("No models were successfully trained.")

            # Identify the best model
            best_model_score = max(model_report.values())
            best_model_name = max(model_report, key=model_report.get)
            best_model = models[best_model_name]

            logging.info(f"Best model identified: {best_model_name} with R2 score: {best_model_score}")

            # Validate the best model's performance
            if best_model_score < 0.6:
                raise CustomException("No suitable model found with R2 score > 0.6.")

            # Save the best model
            os.makedirs(os.path.dirname(self.model_trainer_config.trained_model_file_path), exist_ok=True)
            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )
            logging.info(f"Best model saved to {self.model_trainer_config.trained_model_file_path}")

            # Predict on the test set
            logging.info("Generating predictions on the test set.")
            y_pred = best_model.predict(X_test)
            r2 = r2_score(y_test, y_pred)

            logging.info(f"Model evaluation completed. R2 score: {r2}")
            return r2

        except Exception as e:
            logging.error(f"Error during model training: {str(e)}")
            raise CustomException(e, sys)


if __name__ == "__main__":
    try:
        from src.utils import load_numpy_array

        # Load training and test arrays
        train_array_path = os.path.join('artifacts', 'train_array.npy')
        test_array_path = os.path.join('artifacts', 'test_array.npy')

        train_array = load_numpy_array(train_array_path)
        test_array = load_numpy_array(test_array_path)

        # Initialize and train the model
        model_trainer = ModelTrainer()
        r2_score_value = model_trainer.initiate_model_training(train_array, test_array)

        logging.info(f"Model training completed successfully. Final R2 score: {r2_score_value}")

    except Exception as e:
        logging.error(f"Model training pipeline failed: {str(e)}")