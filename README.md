# 📊 Employee Performance Predictor using Data Analytics

This project focuses on **Workforce Analytics** (People Analytics). It identifies patterns in employee behavior and performance to help HR leaders make data-driven decisions regarding promotions, training, and resource allocation.

## 🎯 Project Objective
To analyze employee data (Training Hours, Projects, Experience, Awards) and identify the "Success DNA"—the specific factors that lead to high-performance ratings within the organization.

## 🔍 Key Analytics Components
* **Correlation Analysis:** Determining the relationship between training investments and performance output.
* **Feature Contribution:** Using statistical weights to identify the most impactful KPIs (Key Performance Indicators).
* **Comparative Analytics:** Comparing different departments (Sales vs. Tech) to see where performance peaks.
* **Performance Categorization:** Using data logic to segment the workforce into "High Potential," "Steady Performers," and "At-Risk" groups.

## 📁 Analysis Workflow
1.  **Data Generation:** Simulating realistic HR metrics for 1,000 employees.
2.  **Data Cleaning:** Handling categorical variables and normalizing metrics.
3.  **Exploratory Data Analysis (EDA):** Visualizing performance drivers.
4.  **Insight Generation:** Producing the "Feature Importance" report to guide HR policy.

## 🛠️ Tools Used
* **Python (Pandas/NumPy):** For data manipulation and cleaning.
* **Matplotlib/Seaborn:** For generating analytical visualizations.
* **Scikit-Learn:** Used here as an **Analytical Engine** to calculate feature weights.
## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Libraries:** Pandas, Scikit-Learn, Seaborn, Matplotlib
* **Environment:** Virtual Environment (venv)

## 📁 Project Structure
- `data/`: Contains the generated employee dataset.
- `models/`: Saved ML models (.pkl).
- `outputs/`: Visualization charts (Feature Importance).
- `src/`: Source code for data generation.

## 🎯 Results
- **Model Accuracy:** 90%+ (Approx)
- **Primary Drivers:** Training Hours and Last Year's Rating were the strongest predictors.

## 💻 How to Run
1. `pip install -r requirements.txt`
2. `python src/data_generator.py`
3. `python main.py`