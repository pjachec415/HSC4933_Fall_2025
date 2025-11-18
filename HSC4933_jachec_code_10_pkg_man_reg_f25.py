#########################################################
# A simple exercise in importing packages using the     #
# package manager and using them to perform regression. #
#########################################################
# H. Jachec # HSC 4933 # Sec. 002 # 11/5/2025 # Code 10 #
#########################################################


# Import Packages
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# Define Data & load pd.DataFrame
data = {
    'Age': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],
    'BloodPressure': [120, 122, 126, 128, 130, 133, 135, 138, 142, 145, 150, 155, 160, 165, 170, 175]
}
df = pd.DataFrame(data)


# Basic Data Exploration
print("Basic Data Exploration:")
print("\nShape (rows, columns):", df.shape)
print("\n Column Types:")
print(df.dtypes)
print("\n Missing Values per Column:")
print(df.isnull().sum())
print("\nSummary Statistics:")
print(df.describe())


# Scatterplot in plt
plt.figure(figsize=(7, 5))
plt.scatter(df['Age'], df['BloodPressure'], label='Pt Data')
plt.xlabel("Age (years)")
plt.ylabel("Blood Pressure (mmHg)")
plt.title("Age vs. Blood Pressure - Scatter Plot")
plt.grid(True)
plt.legend()
plt.show()


# Prepare Data for Regression
X = df[['Age']]
y = df['BloodPressure']

model = LinearRegression()
model.fit(X, y)

slope = model.coef_[0]
intercept = model.intercept_
print(f"\nRegression Equation: BloodPressure = {slope:.4f} * Age + {intercept:.4f}")


# Perform Regression on top of scatterplot
plt.figure(figsize=(7, 5))
plt.scatter(df['Age'], df['BloodPressure'], label='Pt Data')

y_hat = model.predict(X)
plt.plot(df['Age'], y_hat, label='Regression Line')

plt.xlabel("Age (years)")
plt.ylabel("Blood Pressure (mmHg)")
plt.title("Linear Regression Fit\nAge vs. Blood Pressure - Scatter Plot")
plt.grid(True)
plt.legend()
plt.show()


# Make Predictions Based on Age
example_ages = pd.DataFrame({'Age': [30, 40, 50, 60]})
predicted_bp = model.predict(example_ages)

for age, bp in zip(example_ages['Age'], predicted_bp):
    print(f"Predicted Blood Pressure at Age {age}: {bp:.2f}")