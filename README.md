# Laptop_price_prediction# 💻 Laptop Price Predictor

A Machine Learning web application that predicts the price of a laptop based on its hardware specifications. The project uses a trained regression model and a Streamlit interface for real-time price prediction.

---

## 📌 Project Overview

This project predicts laptop prices using machine learning. Users can select laptop specifications such as brand, RAM, processor, storage, display type, and operating system through an interactive Streamlit application. The trained model estimates the expected laptop price.

---

## 🚀 Features

* Interactive Streamlit web interface
* Real-time laptop price prediction
* Data preprocessing and feature engineering
* Machine Learning regression model
* Clean and responsive user interface

---

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Pickle

---

## 📂 Project Structure

```text
Laptop-Price-Predictor/
│
├── app.py                       # Streamlit application
├── laptop_data.csv              # Dataset
├── pipe.pkl                     # Trained ML pipeline
├── df.pkl                       # Processed dataframe
├── README.md
└── notebook.ipynb               # Model training notebook
```

---
## Dataset Features

The model is trained using the following features:

* Company
* TypeName
* RAM
* Weight
* Touchscreen
* IPS Display
* Pixels Per Inch (PPI)
* CPU Brand
* HDD Capacity
* SSD Capacity
* GPU Brand
* Operating System


## ▶️ Running the Application

Start the Streamlit app:

```bash
streamlit run app.py
```

The application will open in your default web browser at:

```text
http://localhost:8501
```

---

## 🧠 Machine Learning Workflow

1. Data Cleaning
2. Feature Engineering
3. Data Preprocessing
4. Train-Test Split
5. Pipeline Creation
6. Model Training
7. Model Evaluation
8. Model Serialization using Pickle
9. Streamlit Deployment

---

## 📈 Model Input Features

The prediction model expects the following inputs:

* Brand
* Laptop Type
* RAM
* Weight
* Touchscreen
* IPS Display
* Screen Resolution
* Screen Size
* CPU Brand
* HDD Storage
* SSD Storage
* GPU Brand
* Operating System

The application calculates **PPI (Pixels Per Inch)** from the selected screen size and resolution before making predictions.

---

## 📦 Dependencies

* streamlit
* pandas
* numpy
* scikit-learn
* matplotlib
* pickle


## 📷 Application Preview

You can add screenshots of the Streamlit application here.

Example:

```
images/home.png
images/prediction.png
```

---



