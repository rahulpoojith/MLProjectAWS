import pickle
import os
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

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


from sklearn.metrics import r2_score

def evaluate_models(X_train, y_train, X_test, y_test, models):
    """
    Trains and evaluates multiple models and returns their R2 scores.
    
    Args:
        X_train: Training feature set.
        y_train: Training target set.
        X_test: Testing feature set.
        y_test: Testing target set.
        models: Dictionary of models to train and evaluate.
        
    Returns:
        A dictionary with model names as keys and R2 scores as values.
    """
    model_report = {}
    for name, model in models.items():
        try:
            # Train the model
            model.fit(X_train, y_train)
            
            # Predict on the test set
            y_pred = model.predict(X_test)
            
            # Calculate R2 score
            r2 = r2_score(y_test, y_pred)
            model_report[name] = r2
        except Exception as e:
            print(f"Model {name} failed to train due to: {e}")
    return model_report