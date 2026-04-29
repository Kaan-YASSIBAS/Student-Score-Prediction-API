import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Sample dataset
data = {
    "hours_studied": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 3, 6, 8, 2, 9],
    "sleep_hours": [6, 7, 6, 8, 7, 6, 8, 7, 8, 7, 5, 9, 6, 8, 5],
    "attendance_rate": [60, 65, 70, 75, 80, 85, 90, 95, 96, 98, 68, 88, 92, 62, 94],
    "previous_score": [30, 38, 45, 50, 55, 60, 68, 72, 80, 85, 42, 64, 75, 35, 78],
    "exam_score": [35, 42, 50, 57, 62, 68, 75, 80, 88, 92, 47, 72, 82, 40, 86],
}

df = pd.DataFrame(data)

# Define features variables
X = df[[
    "hours_studied",
    "sleep_hours",
    "attendance_rate",
    "previous_score",
]]

# Define target variable
y = df["exam_score"]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
)

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions in the test set
predictions = model.predict(X_test)

# Evaluate the model
mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)

# Print evaluation results
print("=== MODEL EVALUATION ===")
print("Predictions:", predictions)
print("Real values:", y_test.values)
print("Mean Absolute Error:", mae)
print("Mean Squared Error:", mse)

# Save the model to a file
joblib.dump(model, "app/model/student_score_model.pkl")

print("\nModel saved to app/model/student_score_model.pkl")