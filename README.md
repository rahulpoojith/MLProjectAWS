
# Student Score Prediction

This repository contains a project for predicting student scores based on various input features using machine learning techniques. It provides an end-to-end solution, from data preprocessing to model evaluation, for score prediction.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
  - [Prerequisites](#prerequisites)
  - [Installation Steps](#installation-steps)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Key Scripts](#key-scripts)
  - [Core Scripts](#core-scripts)
  - [Modules and Pipelines](#modules-and-pipelines)
  - [Logs Directory](#logs-directory)
  - [Notebooks Directory](#notebooks-directory)
  - [MLprojectAWS.egg-info](#mlprojectawsegg-info)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The goal of this project is to develop a machine learning model that can predict the scores of students based on input features like study hours, attendance, or other relevant factors. The project demonstrates data preprocessing, feature engineering, model training, and evaluation.

## Features

- Data preprocessing, including handling missing values and feature scaling.
- Exploratory data analysis (EDA) with visualizations.
- Training various machine learning models and evaluating their performance.
- Hyperparameter tuning for optimized predictions.
- Easy-to-follow project structure and documentation.
- Web interface for inputting student data and predicting scores.

## Technologies Used

- **Python**: Core programming language for the project.
- **Pandas**: For data manipulation and analysis.
- **NumPy**: For numerical computations.
- **Matplotlib and Seaborn**: For data visualization.
- **Scikit-learn**: For machine learning model implementation and evaluation.
- **Flask**: For building the web application.
- **CatBoost and XGBoost**: For advanced machine learning models.

## Setup and Installation

### Prerequisites

- Python 3.8 or higher
- Conda or pip for managing Python packages

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/rahulpoojith/Student-Score-prediction.git
   cd Student-Score-prediction
   ```

2. Create a virtual environment using Conda:
   ```bash
   conda create -n student_score_env python=3.8 -y
   conda activate student_score_env
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the project files:
   ```bash
   python app.py
   ```

## Usage

1. Prepare your dataset by placing it in the `data/` folder. Ensure it follows the format expected by the scripts.
2. Train the preprocessor and model if not already present in the `artifacts/` directory.
3. Run `app.py` to start the Flask web application:
   ```bash
   python app.py
   ```
4. Open your browser and navigate to:
   ```plaintext
   http://127.0.0.1:5001/
   ```
5. Enter the student details (e.g., gender, reading score) and get the predicted math score.

## Project Structure

```
Student-Score-prediction/
├── app.py                     # Main Flask application
├── application.py             # Additional app functionality (if any)
├── data/
│   └── student_scores.csv      # Placeholder for the dataset
├── notebooks/
│   ├── EDA.ipynb               # Jupyter notebook for exploratory data analysis
│   ├── model_training.ipynb    # Jupyter notebook for training the model
│   ├── catboost_info/          # Directory for CatBoost-specific logs and files
│   │   ├── learn/              # Contains training logs and events
│   │   │   ├── events.out.tfevents # TensorFlow event logs
│   │   ├── tmp/                # Temporary files generated during training
│   │   ├── catboost_training.json # CatBoost training configuration
│   │   ├── learn_error.tsv     # Training error logs
│   │   ├── time_left.tsv       # Time left for training
│   └── Data/                   # Additional data files for notebooks
├── src/
│   ├── components/             # Modules for data ingestion, transformation, and model training
│   │   ├── data_ingestion.py   # Data ingestion module
│   │   ├── data_transformation.py # Data transformation module
│   │   ├── model_trainer.py    # Model training module
│   ├── pipelines/              # Prediction and training pipelines
│   │   ├── predict_pipeline.py # Prediction pipeline
│   │   ├── train_pipeline.py   # Training pipeline
│   ├── exception.py            # Custom exception handling module
│   ├── logger.py               # Logging module for tracking events
│   ├── utils.py                # Utility functions for common tasks
├── artifacts/
│   ├── preprocessors.pkl       # Preprocessing pipeline
│   ├── model.pkl               # Trained machine learning model
├── static/                     # CSS, JS, or other assets (optional)
├── templates/
│   ├── index.html              # Landing page
│   ├── home.html               # Prediction form
├── logs/                       # Directory for storing log files
├── MLprojectAWS.egg-info/      # Metadata and dependency files
│   ├── dependency_links.txt    # Dependency links
│   ├── PKG-INFO                # Package metadata
│   ├── requires.txt            # Required dependencies
│   ├── SOURCES.txt             # Source files list
│   ├── top_level.txt           # Top-level package names
├── requirements.txt            # List of dependencies
├── setup.py                    # Python package setup file
├── config.py                   # Configuration file for parameters
└── README.md                   # Project documentation
```

## Key Scripts

### Core Scripts

#### `app.py`
The core application script that:
- Sets up Flask routes for the home page and predictions.
- Loads the trained model and preprocessing pipeline.
- Processes input data and returns predictions.

#### `setup.py`
A Python packaging file for installing the project as a package.

#### `requirements.txt`
Specifies the dependencies required to run the project.

### Modules and Pipelines

#### `src/components/`
Modules for handling key processes:
- `data_ingestion.py`: Handles loading and preprocessing raw data.
- `data_transformation.py`: Applies scaling and encoding to data.
- `model_trainer.py`: Trains and saves machine learning models.

#### `src/pipelines/`
Predefined pipelines for:
- `predict_pipeline.py`: Handling data input and prediction workflow.
- `train_pipeline.py`: Training the model and saving artifacts.

### Logs Directory
- `logs/`: Stores log files generated during execution, helping with debugging and monitoring.

### Notebooks Directory
- `catboost_info/`: Contains logs, configurations, and error tracking files generated by CatBoost.
  - `learn/`: Stores TensorFlow event logs from CatBoost training.
  - `tmp/`: Temporary files used during the training process.
  - `catboost_training.json`: Configuration file for the CatBoost training.
  - `learn_error.tsv`: Error logs during model training.
  - `time_left.tsv`: Estimated time left for training completion.
- `Data/`: Holds additional data files used in Jupyter notebooks.

### MLprojectAWS.egg-info
- Contains metadata and dependency information for the project.
  - `dependency_links.txt`: Additional dependency sources.
  - `PKG-INFO`: Package metadata.
  - `requires.txt`: Lists dependencies.
  - `SOURCES.txt`: List of source files.
  - `top_level.txt`: Top-level package names.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Description of changes"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

AWS deplyment
