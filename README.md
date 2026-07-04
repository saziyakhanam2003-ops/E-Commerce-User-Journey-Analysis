# 🛒 E-Commerce User Journey Funnel Analysis
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-025E8C?style=for-the-badge)
![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)

An end-to-end Data Analytics project that simulates a real-world e-commerce business workflow using *Python, PostgreSQL, SQL, Power BI, and DAX*.

Instead of using a public dataset, I generated a realistic customer journey dataset from scratch using Python and built an interactive Power BI dashboard to analyze user behavior, conversion performance, revenue trends, and customer drop-offs across the purchase funnel.

---

# 📌 Project Overview

This project focuses on understanding how users interact with an e-commerce website—from viewing products to completing purchases.

The objective is to identify customer behavior patterns, conversion bottlenecks, revenue drivers, and business opportunities using SQL and Power BI.

---

# 🎯 Business Questions Solved

- Which traffic source generates the highest conversions?
- Which product category generates the highest revenue?
- Where do customers abandon the purchase journey?
- Which cities contribute the highest revenue?
- How do gender and device influence conversion?
- What is the overall conversion rate?
- What is the cart abandonment rate?

---

# 🛠️ Tech Stack

- Python
- PostgreSQL
- SQL
- Power BI
- DAX
- Excel

---

# 📂 Dataset Generation

Unlike most portfolio projects that use public datasets, this project uses a *custom-generated dataset* created with Python.

The dataset simulates realistic customer behavior throughout an online shopping journey.

### Dataset Includes

- 100,000+ User Sessions
- User IDs
- Session IDs
- Visit Date & Time
- City
- Gender
- Age Group
- Device Type
- Traffic Source
- Product Category
- Product Name
- Product Price
- Discount
- Pages Viewed
- Session Duration
- Product Views
- Add to Cart
- Checkout
- Payment
- Purchase Status
- Cart Value
- Customer Satisfaction

---

# ⚙️ Project Workflow

### Step 1 — Python

- Generated a realistic e-commerce dataset
- Simulated customer journeys
- Exported the dataset as CSV

↓

### Step 2 — PostgreSQL

- Created database
- Imported CSV
- Verified data integrity

↓

### Step 3 — SQL

Performed:

- Data Validation
- Data Cleaning
- Business Analysis
- Revenue Analysis
- Funnel Analysis
- Customer Analysis

↓

### Step 4 — Power BI

- Connected PostgreSQL
- Built DAX Measures
- Created Interactive Dashboard
- Added Dynamic Filters

---

# 📊 Dashboard Pages

## Page 1 — Executive Overview

KPIs

- Total Users
- Total Sessions
- Total Revenue
- Total Purchases
- Conversion Rate
- Cart Abandonment Rate
- Average Order Value
- Average Customer Rating

Visuals

- Revenue by Product Category
- Traffic Source Distribution
- Monthly Purchase Trend
- Gender Distribution

---

## Page 2 — User Journey Funnel Analysis

KPIs

- Product Views
- Add To Cart
- Checkout Started
- Purchases Completed

Visuals

- Customer Purchase Funnel
- Traffic Source Drop-offs
- Monthly Conversion Trend
- Conversion Rate by Device
- Revenue by City & Product Category

---

# 🧮 SQL Analysis

The project includes SQL queries for:

- Database Creation
- Data Validation
- Duplicate Checks
- NULL Value Checks
- Business KPIs
- Revenue Analysis
- Product Analysis
- Device Analysis
- Gender Analysis
- Traffic Source Analysis
- Customer Funnel Analysis
- Window Functions
- Common Table Expressions (CTEs)

---

# 📈 DAX Measures

The dashboard includes custom DAX measures such as:

- Total Users
- Total Sessions
- Total Revenue
- Total Purchases
- Conversion Rate
- Add To Cart Rate
- Checkout Rate
- Cart Abandonment Rate
- Average Order Value
- Average Session Duration
- Average Customer Rating
- Bounce Rate

---

# 💡 Key Business Insights

- Google generated the highest customer traffic.
- Electronics contributed the largest share of revenue.
- A significant number of users abandoned their carts before completing purchases.
- Mobile users showed the highest purchase activity.
- Conversion rates varied across traffic sources and devices.
- Revenue distribution differed across cities and product categories.

---

# 📁 Project Structure


User_Journey_Funnel_Analysis
│
├── Dataset
│   └── user_journey_funnel_dataset.csv
│
├── Images
│   ├── Dashboard_Page_1.png
│   └── Dashboard_Page_2.png
│
├── Power BI
│   └── User_Journey_Funnel_Analysis.pbix
│
├── Python
│   ├── dataset_generation.py
│   ├── dataset_generation.ipynb
│   └── requirements.txt
│
├── SQL
│   ├── 01_database.sql
│   ├── 02_data_cleaning.sql
│   └── 03_business_queries.sql
│
├── README.md
└── LICENSE


---

# 🚀 How to Run

1. Generate or use the provided dataset.
2. Import the CSV into PostgreSQL.
3. Execute the SQL scripts.
4. Open the Power BI (.pbix) file.
5. Refresh the data connection.
6. Explore the interactive dashboard.

---

# 📸 Dashboard Preview

## Executive Overview

(Add Page 1 Screenshot Here)

---

## User Journey Funnel Analysis

(Add Page 2 Screenshot Here)

---

# 🔮 Future Improvements

- Customer Segmentation
- RFM Analysis
- Customer Lifetime Value (CLV)
- Predictive Purchase Analysis
- Marketing Campaign Performance
- Churn Prediction
- Recommendation System

---

# 👨‍💻 Author

*Saziya*

If you found this project useful, consider giving it a ⭐ on GitHub.