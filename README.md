# Local-Food-Wastage-Management-Dashboard
A data-driven food redistribution platform designed to reduce food wastage by connecting food providers with receiver organizations. The project leverages SQL, Python, Streamlit, and Data Analytics to monitor food donations, track claims, generate business insights, and support data-driven decision-making.

# 🔗 Live Dashboard:
https://local-food-wastage-management-dashboard.streamlit.app

# 📌 Problem Statement
Large quantities of edible food are wasted daily due to overproduction, inventory issues, and event leftovers, while many individuals and communities continue to face food insecurity.

# Key challenges include:
Lack of coordination between food donors and receivers
Food expiring before reaching those in need
Absence of real-time monitoring and analytics
Limited visibility into food donation and claim patterns

# 🎯 Project Objectives
Analyze food donation and claim data
Identify major food providers and receiver organizations
Monitor food availability and claim status
Reduce food wastage through efficient redistribution
Build interactive dashboards for decision-making
Generate business insights using SQL and Python

# 🚀 Proposed Solution
The Local Food Wastage Management platform enables:

Tracking of food listings and donations
Monitoring of food claims and fulfillment status
Analysis of provider and receiver activities
Real-time visualization through dashboards
Data-driven recommendations to improve redistribution efficiency

# 📊 Dataset Description
The project uses four datasets containing 4,000 total records.

Dataset	Rows	Columns
Providers	1000	6
Receivers	1000	5
Food Listings	1000	9
Claims	1000	8

# 1. Providers Dataset

Contains information about food donors.

Columns
Provider_ID
Name
Type
Address
City
Contact

# 2. Receivers Dataset

Contains information about food receivers.

Columns
Receiver_ID
Name
Type
City
Contact

# 3. Food Listings Dataset

Contains information about available food donations.

Columns
Food_ID
Food_Name
Quantity
Expiry_Date
Provider_ID
Provider_Type
Location
Food_Type
Meal_Type

# 4. Claims Dataset

Contains food request and claim records.

Columns
Claim_ID
Food_ID
Receiver_ID
Status
Timestamp
Year
Month
Day

# 🧹 Data Cleaning
Missing Values

All datasets were checked for null values.

Dataset	Missing Values
Providers	0
Receivers	0
Food Listings	0
Claims	0
Result

✅ No missing values found.

Duplicate Records

Duplicate records were verified across all datasets.

Dataset	Duplicates
Providers	0
Receivers	0
Food Listings	0
Claims	0
Result

✅ No duplicate records found.

Data Type Validation

Date columns were converted for analysis:

food['Expiry_Date'] = pd.to_datetime(food['Expiry_Date'])
claims['Timestamp'] = pd.to_datetime(claims['Timestamp'])
Data Types
Providers
Column	Type
Provider_ID	Integer
Name	Text
Type	Text
Address	Text
City	Text
Contact	Text
Receivers
Column	Type
Receiver_ID	Integer
Name	Text
Type	Text
City	Text
Contact	Text
Food Listings
Column	Type
Food_ID	Integer
Food_Name	Text
Quantity	Integer
Expiry_Date	Date
Provider_ID	Integer
Provider_Type	Text
Location	Text
Food_Type	Text
Meal_Type	Text
Claims
Column	Type
Claim_ID	Integer
Food_ID	Integer
Receiver_ID	Integer
Status	Text
Timestamp	DateTime
Year	Integer
Month	Integer
Day	Integer

# 📈 Exploratory Data Analysis (EDA)
Dataset Overview
Dataset	Records	Columns
Providers	1000	6
Receivers	1000	5
Food Listings	1000	9
Claims	1000	8

Total Records Analyzed: 4,000

Food Type Distribution
Food Type	Listings
Vegetarian	336
Vegan	334
Non-Vegetarian	330
Insight

Food donations are almost equally distributed across all food categories, demonstrating support for diverse dietary preferences.

Claim Status Analysis
Status	Claims
Completed	339
Cancelled	336
Pending	325
Insight

Completed claims slightly exceed cancelled and pending claims, indicating effective redistribution with room for operational improvements.

Outlier Detection
Quantity Analysis
Box plots were used to evaluate food quantity distributions.
No significant outliers were detected.
Insight

Food donation quantities remain within expected operational ranges.

Correlation Analysis

A correlation matrix was generated for numerical variables.

Findings
Most numerical columns are identifiers.
Weak correlations observed.
No strong linear relationships identified.
Insight

Correlation analysis has limited business relevance due to the predominance of ID-based fields.

Seasonality Analysis
Observation

The available data contains records only for March 2025.

Insight

Seasonality cannot be determined from a single month of data. Daily fluctuations within March were analyzed instead.

# 🗄️ SQL Business Insights

The project includes SQL queries that generate actionable business insights.

Key Analyses
1. Total Food Available

Calculates total food quantity currently available for redistribution.

2. Total Food Listings

Measures the total number of food donation listings.

3. Provider Type Distribution

Identifies which provider categories contribute the most food.

4. Top 10 Providers by Quantity Donated

Highlights the largest contributors.

5. Food Quantity by Meal Type

Analyzes donation volume by meal category.

Insight: Snacks are donated most frequently.

6. Food Quantity by Food Type

Analyzes donation volume by food category.

Insight: Vegan food is most available.

7. Average Quantity per Listing

Evaluates average donation quantity.

8. Most Common Food Items

Identifies the most frequently donated foods.

9. Claims Status Summary

Analyzes completed, pending, and cancelled claims.

10. Claim Success Rate

Measures the effectiveness of food request fulfillment.

# 📊 Dashboard Features
KPI Cards
Total Providers
Total Receivers
Total Listings
Total Claims
Total Food Quantity
Claim Success Rate
Visualizations
Visualization	Purpose
Pie Chart	Claim Status Distribution
Column Chart	Provider Type Distribution
Column Chart	Food Category Distribution
Pie Chart	Meal Type Distribution
Column Chart	Receiver Distribution
Bar Chart	Top Provider Cities
Scatter Plot	Monthly Claims Trend
Scatter Plot	Monthly Listings Trend
Bar Chart	Most Claimed Food Items

🛠️ Technology Stack
Programming & Analytics
Python
Pandas
NumPy
SQL
Data Visualization
Matplotlib
Seaborn
Plotly
Dashboard
Streamlit
Database
SQL Database (MySQL/SQLite)

# Clone the repository:
git clone https://github.com/your-username/local-food-wastage-management.git

Navigate to the project directory:
cd local-food-wastage-management

Install dependencies:
pip install -r requirements.txt

Run the Streamlit dashboard:
streamlit run app.py

# 📌 Business Recommendations
Increase Claim Completion Rate
Automate claim assignment
Send expiry notifications
Improve claim workflow tracking
Reduce Food Wastage
Prioritize food nearing expiry
Implement smart matching algorithms
Enable real-time availability updates
Improve Receiver Engagement
Instant notifications for new listings
Mobile-friendly claim tracking
Faster claim approval process
Enhance Analytics
Real-time dashboards
Predictive demand forecasting
Provider and receiver performance metrics

# ✅ Conclusion
The Local Food Wastage Management project demonstrates how data analytics can help reduce food waste and improve food redistribution. Through SQL analysis, Python-based EDA, and Streamlit visualizations, stakeholders can monitor donations, track claims, identify inefficiencies, and make informed decisions.

The analysis highlights:

Strong participation from food providers
Balanced food category distribution
Effective redistribution processes
Opportunities to improve claim completion rates and operational efficiency

By leveraging analytics and visualization, the platform contributes toward a more sustainable and efficient food donation ecosystem.

# 📷 Dashboard

Live Application:

👉 https://local-food-wastage-management-dashboard.streamlit.app
