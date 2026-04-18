# 📊 Employee Performance Predictor 

This project uses **Machine Learning** to help HR departments identify high-performing employees and predict performance categories based on historical data.

## 🚀 Key Features
* **Synthetic Data Simulation:** Realistic generation of 1,000+ employee records.
* **Predictive Modeling:** Uses a **Random Forest Classifier** to categorize performance.
* **Feature Importance:** Identifies the top factors (like Awards or Projects) that drive performance.

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