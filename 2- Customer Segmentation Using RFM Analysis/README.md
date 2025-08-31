# 🛍️ Customer Segmentation using RFM Analysis  

## 📌 Project Description  
This project performs **Customer Segmentation** using the **RFM (Recency, Frequency, Monetary) Analysis** technique on the **Online Retail Dataset (UCI)**.  
The goal is to analyze customer purchasing behavior and group customers into different segments for better marketing strategies.  

---

## 📂 Dataset  
- **Source**: [UCI Online Retail Dataset](https://archive.ics.uci.edu/ml/datasets/online+retail)  
- **Period**: December 2010 – December 2011  
- **Description**:  
  - Transactions from a UK-based online retail store.  
  - Includes details like Invoice Number, Product Description, Quantity, Invoice Date, Unit Price, Customer ID, and Country.  

---

## 🔑 RFM Analysis  
We calculate three key metrics for each customer:  
- **Recency (R):** How recently a customer purchased.  
- **Frequency (F):** How often a customer purchased.  
- **Monetary (M):** How much money a customer spent.  

Each metric is scored (1–4), then combined into an **RFM score** for segmentation.  

---

## 📊 Exploratory Data Analysis (EDA)  
Before segmentation, we explored the dataset with different visualizations:  
- 📈 **Monthly Sales Trend**  
- 🌍 **Top Countries by Sales**  
- 🛒 **Distribution of Order Value & Basket Size per Customer**  
- 🏷️ **Top Products by Sales**  
- ⏰ **Transactions by Day of Week & Hour of Day**  

---

## 📌 Customer Segments  
Customers are segmented based on their RFM score, e.g.:  
|       Segment       | Count
|---------------------|------
|Loyal Customers      | 1302
|Potential Loyalist   |  919
|Needs Attention      |  908
|Champions            |  838
|Others               |  371

---

## 🛠️ Tools & Libraries  
- **Python** – Data wrangling and RFM scoring (Pandas, NumPy)
- **Pandas** – Data manipulation  
- **Seaborn & Matplotlib** – Data visualization  
- **Jupyter Notebook** – Analysis & reporting  

---

## ✨ Author  
👤 Ahmed – Data Engineering Enthusiast  
