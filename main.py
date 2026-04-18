import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib

# 1. Load Data
df = pd.read_csv('data/employee_data.csv')

# 2. Basic Cleaning & Encoding
# Convert 'Department' text into numbers so the AI can understand it
df_encoded = pd.get_dummies(df, columns=['Department'], drop_first=True)

# 3. Define Features (X) and Target (y)
X = df_encoded.drop(['Employee_ID', 'Performance_Category'], axis=1)
y = df_encoded['Performance_Category']

# 4. Split Data (80% for training, 20% for testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Build the Model
print("🚀 Training the Performance Predictor Model...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 6. Evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"🎯 Model Accuracy: {accuracy * 100:.2f}%")
print("\nDetailed Report:\n", classification_report(y_test, y_pred))

# 7. Save the Model and Visuals
joblib.dump(model, 'models/performance_model.pkl')

plt.figure(figsize=(10,6))
sns.barplot(x=model.feature_importances_, y=X.columns)
plt.title("Key Factors Driving Employee Performance")
plt.savefig('outputs/feature_importance.png')
print("📊 Chart saved to outputs/feature_importance.png")