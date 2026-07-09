# 📊 Marketing Campaign Performance Analysis API

## Project Overview

The **Marketing Campaign Performance Analysis API** is a backend-focused data analytics project built using **Python**, **FastAPI**, **NumPy**, **Pandas**, **Matplotlib**, and **Seaborn**. Rather than providing its own user interface, the project exposes RESTful API endpoints that perform data analysis and return structured JSON responses, making it easy to integrate with any frontend or third-party application.

The API processes marketing campaign datasets to generate statistical summaries, calculate key performance indicators (KPIs), and provide business insights. It also supports generating visualizations that can be returned as image files or downloaded by client applications.

This project demonstrates how traditional data analysis workflows can be transformed into reusable backend services, following a modular architecture suitable for future expansion into machine learning and artificial intelligence.

---

# Project Objectives

* Build a RESTful API for marketing data analysis.
* Load and process CSV marketing datasets.
* Clean and validate incoming data.
* Calculate business performance metrics.
* Generate statistical summaries.
* Create downloadable visualizations.
* Return analysis results in JSON format.
* Design the project for future AI and machine learning integration.

---

# Tech Stack

## Backend

* FastAPI
* Uvicorn

## Data Processing

* NumPy
* Pandas

## Data Visualization

* Matplotlib
* Seaborn

## Validation

* Pydantic

## File Handling

* CSV

---

# Features

* Upload marketing campaign datasets.
* Automatic data validation and cleaning.
* Calculate:
  * Revenue
  * Marketing Cost
  * ROI
  * Click Through Rate (CTR)
  * Conversion Rate
* Campaign performance analysis.
* Channel performance analysis.
* Customer demographic analysis.
* Monthly revenue trends.
* Correlation analysis.
* Generate visualization images.
* Return structured JSON responses.

---

# Project Structure

```text
marketing-campaign-analysis-api/
│
├── app/
│   │
│   ├── main.py                 # FastAPI application
│   │
│   ├── api/
│   │   ├── upload.py
│   │   ├── analysis.py
│   │   ├── visualization.py
│   │   └── metrics.py
│   │
│   ├── services/
│   │   ├── data_loader.py
│   │   ├── preprocessing.py
│   │   ├── feature_engineering.py
│   │   ├── analytics.py
│   │   └── charts.py
│   │
│   ├── models/
│   │   ├── request_models.py
│   │   └── response_models.py
│   │
│   ├── utils/
│   │   └── helpers.py
│   │
│   └── storage/
│       ├── uploads/
│       └── charts/
│
├── data/
│   └── sample_marketing_data.csv
│
├── tests/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# API Workflow

```text
Client
   │
   ▼
FastAPI Endpoint
   │
   ▼
Data Validation
   │
   ▼
Data Cleaning
   │
   ▼
Feature Engineering
   │
   ▼
Statistical Analysis
   │
   ├────────► JSON Response
   │
   └────────► Visualization Generation
                    │
                    ▼
              PNG Image Response
```

---

# Proposed API Endpoints

## Upload Dataset

```
POST /upload
```

Uploads a marketing campaign CSV file for analysis.

---

## Dataset Summary

```
GET /summary
```

Returns:

* Number of records
* Missing values
* Duplicate count
* Data types
* Basic statistics

---

## Campaign Analysis

```
GET /campaigns
```

Returns:

* Revenue by campaign
* Cost by campaign
* ROI
* Conversion Rate

---

## Channel Analysis

```
GET /channels
```

Returns:

* Revenue
* Clicks
* Impressions
* ROI
* CTR

---

## Customer Analysis

```
GET /customers
```

Returns:

* Age distribution
* Gender distribution
* City-wise revenue

---

## Monthly Analysis

```
GET /monthly
```

Returns monthly revenue and campaign performance trends.

---

## Correlation Analysis

```
GET /correlation
```

Returns the correlation matrix for numerical features.

---

## Generate Charts

```
GET /charts/revenue
```

Returns a revenue bar chart.

```
GET /charts/heatmap
```

Returns a correlation heatmap.

```
GET /charts/monthly
```

Returns a monthly revenue line chart.

---

# Sample JSON Response

```json
{
    "campaign": "Summer Sale",
    "revenue": 185000,
    "cost": 72000,
    "roi": 156.94,
    "ctr": 4.82,
    "conversion_rate": 8.13
}
```

---

# Future Expansion

The project is designed to evolve beyond descriptive analytics into intelligent decision support.

Potential additions include:

* Customer Segmentation
* Churn Prediction
* Campaign Success Prediction
* Sales Forecasting
* Recommendation System
* Marketing Performance Dashboard
* LLM-powered Business Insight Generator
* Deep Learning Models for Customer Behavior Prediction

---

# Learning Outcomes

By completing this project, you will gain experience in:

* REST API development with FastAPI
* Data preprocessing with Pandas
* Numerical computing with NumPy
* Data visualization using Matplotlib and Seaborn
* API design and response modeling
* Backend architecture for data science applications
* Building scalable analytics services ready for machine learning integration

---

# Future Frontend Compatibility

Since the project follows an API-first architecture, it can be integrated with:

* React
* Angular
* Vue.js
* Flutter
* Streamlit
* Power BI
* Tableau
* Mobile Applications
* Any client capable of making HTTP requests
# Marketing-API
