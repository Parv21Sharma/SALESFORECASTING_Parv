# 📊 End-to-End Sales Forecasting & Demand Intelligence System

## Overview

This project was developed as part of an AI & Data Science Internship (Week 3 & Week 4). It focuses on building an intelligent sales forecasting and demand intelligence system using historical sales data.

The system performs data preprocessing, exploratory data analysis, time series forecasting, anomaly detection, product demand segmentation, and presents the results through an interactive Streamlit dashboard.

---

## Project Objectives

- Forecast future sales using multiple forecasting models.
- Compare forecasting performance using evaluation metrics.
- Detect unusual sales patterns using anomaly detection techniques.
- Segment products into demand-based clusters.
- Visualize insights through an interactive dashboard.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Statsmodels (SARIMA)
- Prophet
- XGBoost
- Streamlit

---

## Project Structure

```
SalesForecasting_Parv/
│
├── app.py
├── analysis.ipynb
├── train.csv
├── requirements.txt
├── README.md
│
├── charts/
│   ├── sarima_forecast.png
│   ├── prophet_forecast.png
│   ├── xgboost_forecast.png
│   ├── zscore_anomalies.png
│   ├── isolation_forest_anomalies.png
│   ├── elbow_method.png
│   ├── product_clusters.png
│   └── ...
```

---

## Features

### 📈 Exploratory Data Analysis
- Dataset exploration
- Sales trends
- Category-wise analysis
- Region-wise analysis
- Shipping analysis

### 🔮 Sales Forecasting
- SARIMA
- Prophet
- XGBoost
- Model performance comparison

### 🚨 Anomaly Detection
- Z-Score based anomaly detection
- Isolation Forest anomaly detection

### 📦 Product Clustering
- Feature engineering
- K-Means clustering
- Elbow Method
- Demand segmentation

### 🌐 Interactive Dashboard
Developed using Streamlit with:
- Dataset overview
- Forecast visualization
- Anomaly detection results
- Product clustering insights

---

## Installation

Clone the repository:

```bash
git clone <repository-link>
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## Results

- Successfully forecasted future sales using three forecasting models.
- Compared forecasting accuracy using MAE, RMSE, and MAPE.
- Identified abnormal sales periods using statistical and machine learning techniques.
- Segmented products into demand-based clusters using K-Means.
- Developed an interactive dashboard for business insights.

---

## Future Improvements

- Real-time forecasting
- Automated model retraining
- Database integration
- Cloud deployment
- Interactive filtering options

---

## Author

**Parv Sharma**

AI & Data Science Internship Project
