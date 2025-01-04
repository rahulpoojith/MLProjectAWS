import pickle
import os

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
