import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

import joblib


# 1. Load the dataset
data = pd.read_csv("data/landslide_data.csv")

print("Dataset loaded successfully!")
print(data)


# 2. Select the input features
X = data[
    [
        "rainfall",
        "soil_moisture",
        "slope",
        "previous_landslides",
        "elevation"
    ]
]


# 3. Select the target/output
y = data["risk"]


# 4. Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# 5. Create the Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# 6. Train the model
model.fit(X_train, y_train)

print("Model trained successfully!")


# 7. Test the model
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("Model Accuracy:", accuracy)


# 8. Save the trained model
joblib.dump(model, "model/landslide_model.pkl")

print("Model saved successfully!")