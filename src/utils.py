import os
import pickle
import dill

def save_object(file_path, obj):
    """
    Saves a Python object as a pickle file to the specified path.
    """
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'wb') as file:
            pickle.dump(obj, file)
    except Exception as e:
        raise Exception(f"Error saving object to {file_path}: {str(e)}")

def load_object(file_path):
    """
    Loads a Python object from a pickle file.
    """
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"{file_path} does not exist.")
        with open(file_path, 'rb') as file_obj:
            return dill.load(file_obj)
    except Exception as e:
        raise Exception(f"Error loading object from {file_path}: {str(e)}")