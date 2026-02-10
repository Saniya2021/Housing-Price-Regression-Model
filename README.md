# 🏠 Housing Price Regression Model

This repository contains a Python-based machine learning project focused on **Linear Regression**. The goal of the project is to model the relationship between **house size** and **house price**, train a regression model using real data, and visualize both the original data and the model’s predictions.

---

## 📂 Project Contents

The repository includes the following files:

- **home-price-regression.py** – The main Python script that loads the dataset, trains the model, and visualizes the results.  
- **home_dataset.csv** – The dataset containing house sizes and their corresponding prices.  
- **README.md** – Project documentation.

---

## 🎯 Project Overview

This project demonstrates the following machine learning and data analysis concepts:

- 📊 Loading and manipulating data using pandas and NumPy  
- 📈 Visualizing data using matplotlib  
- 🧠 Training a Linear Regression model using scikit-learn  
- 🧪 Splitting data into training and testing sets (80/20 split)  
- 🔍 Comparing actual values with predicted values using plots  

These concepts are fundamental to supervised machine learning and are widely used in data science and predictive modeling.

---

## 🛠️ Tech Stack

- **Language:** Python  
- **Data Handling:** Pandas, NumPy  
- **Machine Learning:** Scikit-learn (Linear Regression)  
- **Visualization:** Matplotlib  
- **Development Environment:** Any Python IDE (e.g., VS Code, PyCharm, Jupyter)

---

## 🛠️ How to Use

1. **Prepare the Dataset**  
   Make sure `home_dataset.csv` is in the project directory and contains:
   - `HouseSize` – Numeric value representing house size (e.g., square feet)  
   - `HousePrice` – Numeric value representing house price (e.g., in millions of dollars)

2. **Run the Program**  
   Open a terminal in the project folder and run:
   ```bash
   python home-price-regression.py
