# 🔥 Calories Burnt Prediction App

A Machine Learning-based web application that predicts the number of calories burned during exercise based on user body parameters and activity metrics.

Built using Python, Scikit-learn, and deployed using Streamlit.

---

## 📌 Project Overview

This project aims to predict calories burned during physical activity using supervised machine learning techniques. 

The system takes user inputs such as:

- Gender
- Age
- Height
- Weight
- Exercise Duration
- Heart Rate
- Body Temperature

It processes these features through a trained regression model and returns an estimated calorie burn value.

---

## 🚀 Live Features

- Interactive Streamlit web interface
- Real-time prediction
- Clean UI with custom CSS styling
- Gender encoding and structured feature input
- Trained ML model integrated with pickle

---

## 🧠 Machine Learning Workflow

### 1️⃣ Data Collection

The project uses two datasets:

- `exercise.csv`
- `calories.csv`

These datasets were merged and used for training.

### 2️⃣ Data Preprocessing

- Handled structured numerical data
- Encoded categorical variable (Gender)
- Performed feature selection
- Split data into training and testing sets

### 3️⃣ Model Training

Regression models were trained and evaluated using:

- Scikit-learn
- XGBoost

Model evaluation metrics used:
- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)

The best-performing model was saved as:

```

calories_model.pkl

````

### 4️⃣ Deployment

The trained model is loaded in the Streamlit app using:

```python
pickle.load(open("calories_model.pkl", "rb"))
````

The application takes user inputs, converts them into a NumPy array, and generates predictions in real-time.

---

## 🛠️ Tech Stack

**Programming Language**

* Python

**Libraries**

* NumPy
* Pandas
* Scikit-learn
* XGBoost
* Matplotlib
* Seaborn

**Framework**

* Streamlit

(Dependencies listed in requirements.txt )

---

## 📂 Project Structure

```
Calories-Prediction/
│
├── app.py                  # Streamlit web application :contentReference[oaicite:3]{index=3}
├── model1.ipynb            # Model training notebook
├── calories_model.pkl      # Trained ML model
├── exercise.csv            # Exercise dataset
├── calories.csv            # Calories dataset
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```

---

## ⚙️ Installation & Setup

### Step 1: Clone Repository

```bash
git clone https://github.com/yourusername/calories-prediction.git
cd calories-prediction
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run Application

```bash
streamlit run app.py
```

---

## 📊 Input Features Used

| Feature          | Description                  |
| ---------------- | ---------------------------- |
| Gender           | Male / Female (encoded)      |
| Age              | Age in years                 |
| Height           | Height in cm                 |
| Weight           | Weight in kg                 |
| Duration         | Exercise duration in minutes |
| Heart Rate       | Beats per minute             |
| Body Temperature | Temperature in °C            |

---

## 🎯 Project Objectives

* Apply supervised machine learning for real-world prediction
* Implement end-to-end ML pipeline
* Deploy model using Streamlit
* Demonstrate model integration using pickle
* Build a clean and user-friendly ML web app

---

## 📌 Key Highlights

✔ End-to-end ML pipeline
✔ Model training + evaluation
✔ Deployment-ready application
✔ Clean UI design
✔ Structured feature engineering
✔ Reproducible environment

---

## 👩‍💻 Developed By

**Shree Lakshmi**
Machine Learning & Data Analytics Enthusiast

📧 [shreelakshmipp@gmail.com](mailto:shreelakshmipp@gmail.com)

---
