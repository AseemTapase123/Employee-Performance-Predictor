import pandas as pd
import numpy as np
import os

def generate_hr_data(n=1000):
    np.random.seed(42)
    
    # Randomly generating employee attributes
    data = {
        'Employee_ID': range(1001, 1001 + n),
        'Department': np.random.choice(['Sales', 'Tech', 'HR', 'Marketing', 'Finance'], n),
        'Age': np.random.randint(22, 55, n),
        'Experience_Years': np.random.randint(1, 25, n),
        'Projects_Handled': np.random.randint(2, 12, n),
        'Average_Monthly_Hours': np.random.randint(120, 250, n),
        'Last_Performance_Score': np.random.uniform(1.0, 5.0, n).round(1),
        'Awards_Won': np.random.choice([0, 1], n, p=[0.9, 0.1]),
        'Training_Hours': np.random.randint(10, 80, n)
    }
    
    df = pd.DataFrame(data)

    # Creating a logic for the 'Target' (The Performance Category)
    # High score = High projects + High Rating + Awards
    # Low score = High hours (burnout) + Low rating
    perf_score = (df['Last_Performance_Score'] * 2) + (df['Projects_Handled'] * 0.5) + (df['Awards_Won'] * 3) - (df['Average_Monthly_Hours'] * 0.01)
    
    # Define Categories: 0 (Low), 1 (Medium), 2 (High)
    df['Performance_Category'] = pd.cut(perf_score, bins=[-np.inf, 6, 11, np.inf], labels=[0, 1, 2])
    
    # Save to data folder
    output_path = os.path.join('data', 'employee_data.csv')
    df.to_csv(output_path, index=False)
    print(f"✅ Success! Generated {n} employee records at: {output_path}")

if __name__ == "__main__":
    generate_hr_data()