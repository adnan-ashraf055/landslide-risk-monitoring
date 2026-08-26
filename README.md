# 🌍 AI-Based Landslide Risk Monitoring System

An AI/ML-based landslide risk prediction system that predicts the risk of a landslide based on environmental and geographical conditions.

This project is created as a practice implementation for the **Smart India Hackathon (SIH)** problem statement:

> **AI-Based Early Warning and Landslide Risk Monitoring System in North Eastern Region (NER)**

---

## 📌 Problem Statement

Landslides can cause serious damage to people, roads, buildings, and other infrastructure, especially in hilly and mountainous regions.

The goal of this project is to use **Machine Learning** to analyze important environmental factors and predict whether the current conditions indicate a:

- 🟢 LOW risk
- 🟡 MEDIUM risk
- 🔴 HIGH risk

The system can be used as a basic foundation for an early-warning system.

---

## 🎯 Objective

The main objective of this project is:

1. Collect environmental data.
2. Train a Machine Learning model using historical/example data.
3. Accept new environmental information from the user.
4. Analyze the given conditions.
5. Predict the landslide risk.
6. Display the result clearly to the user.

---

## 🧠 How the System Works

The system uses five main inputs:

| Input | Meaning | Example |
|---|---|---|
| Rainfall | Amount of rain received | 190 mm |
| Soil Moisture | Amount of water present in soil | 85% |
| Slope | Steepness of the land | 40° |
| Previous Landslides | Number of previous landslides | 3 |
| Elevation | Height above sea level | 1800 m |

These values are given to the Machine Learning model.

The model analyzes the combination of these values and predicts the landslide risk.

### Basic Flow

```text
User enters environmental data
             ↓
       predict.py
             ↓
   Load trained ML model
             ↓
     Process user inputs
             ↓
    Machine Learning model
             ↓
     Risk Prediction
             ↓
   LOW / MEDIUM / HIGH
