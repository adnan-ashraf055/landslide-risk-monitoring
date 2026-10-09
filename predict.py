import joblib


# Load the trained model
model = joblib.load("model/landslide_model.pkl")


# Ask the user for information
print("================================")
print("   LANDSLIDE RISK CHECKER")
print("================================")

rainfall = float(input("Enter rainfall (mm): "))
soil_moisture = float(input("Enter soil moisture (%): "))
slope = float(input("Enter slope (degrees): "))
previous_landslides = int(input("Enter previous landslides: "))
elevation = float(input("Enter elevation (meters): "))


# Put the user's data into a format the model understands
new_data = [[
    rainfall,
    soil_moisture,
    slope,
    previous_landslides,
    elevation
]]


# Ask the ML model to predict the risk
prediction = model.predict(new_data)


# Convert prediction number into a readable risk level
risk_levels = {
    0: "LOW",
    1: "MEDIUM",
    2: "HIGH"
}

risk = risk_levels[prediction[0]]


# Show the result
print()
print("================================")
print("      RISK ASSESSMENT")
print("================================")

print("Rainfall:", rainfall, "mm")
print("Soil Moisture:", soil_moisture, "%")
print("Slope:", slope, "degrees")
print("Previous Landslides:", previous_landslides)
print("Elevation:", elevation, "meters")

print("--------------------------------")

print("Predicted Risk:", risk)

print("================================")