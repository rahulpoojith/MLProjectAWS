import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from src.utils import save_object

# Load your dataset
data = pd.read_csv('path_to_your_dataset.csv')

# Define features and target
X = data.drop(columns=['math_score'])  # Replace with actual target column
y = data['math_score']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define preprocessor and model
preprocessor = StandardScaler()
model = RandomForestRegressor(random_state=42)

# Create pipeline
pipeline = Pipeline([
    ('scaler', preprocessor),
    ('model', model)
])

# Train the pipeline
pipeline.fit(X_train, y_train)

# Save preprocessor and model separately
save_object('artifacts/preprocessor.pkl', preprocessor)
save_object('artifacts/model.pkl', model)

print("Training complete. Artifacts saved.")