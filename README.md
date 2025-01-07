
# **Student Exam Performance Predictor**

## **Overview**
This project is a web-based application for predicting students' math scores based on demographic and performance data. It leverages a machine learning pipeline for preprocessing input data and making predictions.

## **Key Features**
- Web interface for inputting student data.
- Predicts math scores using trained machine learning models.
- Preprocessing pipeline for scaling numerical features and encoding categorical variables.
- Flask-based backend for serving the application.

---

## **Installation**

### **1. Clone the Repository**
```bash
git clone <repository-url>
cd <repository-folder>
```

### **2. Install Dependencies**
Use the provided `requirements.txt` file to install necessary dependencies:
```bash
pip install -r requirements.txt
```

## **Dependencies**
The key dependencies are listed in `requirements.txt`:
```plaintext
numpy
pandas
scikit-learn
nltk
tensorflow
matplotlib
seaborn
jupyter
catboost
xgboost
Flask
```

---

## **Usage**

### **1. Train the Preprocessor and Model**
- Train the preprocessor (`preprocessors.pkl`) and model (`model.pkl`) if they are not already present in the `artifacts/` directory.
- Use the provided scripts to save these files in the `artifacts/` folder.

### **2. Run the Application**
Start the Flask application:
```bash
python app.py
```

### **3. Access the Web Application**
Open your browser and navigate to:
```plaintext
http://127.0.0.1:5001/
```

### **4. Predict Math Scores**
1. Enter the student's details (e.g., gender, reading score, etc.).
2. Submit the form to get the predicted math score.

---

## **Project Structure**
```
.
├── app.py                     # Main Flask application
├── application.py             # Additional app functionality (if any)
├── requirements.txt           # List of dependencies
├── setup.py                   # Python package setup file
├── templates/
│   ├── index.html             # Landing page
│   ├── home.html              # Prediction form
├── static/                    # CSS, JS, or other assets (optional)
├── artifacts/
│   ├── preprocessors.pkl      # Preprocessing pipeline
│   ├── model.pkl              # Trained machine learning model
```

---

## **Key Scripts**

### **`app.py`**
The core application script that:
- Sets up Flask routes for the home page and predictions.
- Loads the trained model and preprocessing pipeline.
- Processes input data and returns predictions.

### **`setup.py`**
A Python packaging file for installing the project as a package.

### **`requirements.txt`**
Specifies the dependencies required to run the project.

---

## **Notes**

- Ensure the `artifacts/` folder contains `preprocessors.pkl` and `model.pkl` before running predictions.
- If any required files are missing, use the appropriate training scripts to generate them.

---

## **License**
This project is licensed under [MIT License](LICENSE).

---


