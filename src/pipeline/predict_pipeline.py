import pandas as pd
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        """
        Loads the model and preprocessors, and predicts the output.
        """
        try:
            model_path = 'artifacts/model.pkl'
            preprocessors_path = 'artifacts/preprocessor.pkl'

            # Load the model and preprocessors
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessors_path)

            # Transform features and predict
            data_scaled = preprocessor.transform(features)
            pred = model.predict(data_scaled)
            return pred

        except Exception as e:
            raise Exception(f"Error in prediction pipeline: {str(e)}")

class CustomData:
    def __init__(self, gender, race_ethnicity, parental_level_of_education, lunch, 
                 test_preparation_course, reading_score, writing_score):
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score

    def get_data_as_data_frame(self):
        """
        Converts custom data into a pandas DataFrame.
        """
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score]
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise Exception(f"Error in creating data frame: {str(e)}")