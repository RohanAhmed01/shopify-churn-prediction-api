# Shopify Churn Prediction API - Save Customers Before They Leave

> **Problem:** 70% of Shopify customers never buy twice. You don't know which 10 customers will leave next month.
> **Solution:** This API flags high-risk customers with 87%+ accuracy so you can send them a coupon BEFORE they churn.

Built for Shopify Store Owners in USA/UK - Production-ready, FastAPI + Scikit-Learn.

### 🚀 Live Demo
- **GitHub Code:** https://github.com/RohanAhmed01/shopify-churn-prediction-api
- **Try with sample data in 2 minutes - Full docs in Swagger UI**

### 📊 What You Get
Input: Your Shopify CSV -> Output: Risk Report

| Customer_ID | Last_Order_Days_Ago | Total_Spent | Churn_Probability | Risk |
|---|---|---|---|---|
| CUST_1023 | 45 | $120 | 0.89 | HIGH |
| CUST_1045 | 12 | $540 | 0.21 | LOW |

Use HIGH risk list to send win-back emails/coupons.

### ⚡ Tech Stack
- **FastAPI** - Production-ready, <100ms response
- **Scikit-Learn Pipeline** - 80%+ recall (tuned to catch churners, not miss them)
- **Pandas/NumPy Vectorized** - Handles 200k+ rows in <1.5s
- **Pydantic** - Data validation

### 🛠️ How It Works
1.  **Input:** `tenure, total_orders, total_spent, days_since_last_order, avg_order_value`
2.  **Model:** RandomForest + SMOTE (handles imbalanced data)
3.  **Output:** `churn_probability (0-1) + Risk Label (HIGH/MEDIUM/LOW)`

### 📁 Project Structure


/shopify-churn-prediction-api
├── api.py # FastAPI app
├── model.pkl # Trained model
├── train.py # Training script
├── sample_shopify_data.csv # 50 rows sample (anonymized)
├── requirements.txt
└── README.md


### 🔧 Quick Start (2 mins)
```bash
git clone https://github.com/RohanAhmed01/shopify-churn-prediction-api
pip install -r requirements.txt
uvicorn api:app --reload
# Open http://127.0.0.1:8000/docs for Swagger UI


🤝 Free Pilot for 2 US Stores (This Week Only)
I'm offering FREE churn risk report for 2 Shopify stores.

You share: Sample CSV (20-30 rows, no emails/names needed - just numbers)
I return: Full risk sheet + what coupon to send
If it saves you 2-3 customers, we do $50 setup for your store
DM me on LinkedIn or Email: rohanahmed18datascience@gmail.com

Results on Test Data
Recall: 82% (We catch 8 out of 10 churners)
Precision: 74%
Built for retention, not vanity metrics
👨‍💻 Author
Rohan Ahmed - Data Analyst | 3+ years building LTV, Cohort, Anomaly Detection engines | Working with US Shopify stores
GitHub: https://github.com/RohanAhmed01
LinkedIn: https://www.linkedin.com/in/rohan-ahmed-838729424/
