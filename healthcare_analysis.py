A. Analyzing Calorie Distribution
import pandas as pd
import matplotlib.pyplot as plt

# Load your healthcare data
df = pd.read_csv('health_logs.csv')

# 1. Distribution of Calorie Intake
plt.hist(df['Daily Calorie Intake'], bins=range(0, 5000, 500), color='skyblue', edgecolor='black')
plt.title('Distribution of Daily Calorie Intake')
plt.xlabel('Calories')
plt.ylabel('Number of Users')
plt.show()

# 2. Descriptive Statistics
mean_cal = df['Daily Calorie Intake'].mean()
median_cal = df['Daily Calorie Intake'].median()
std_cal = df['Daily Calorie Intake'].std()

print(f"Mean: {mean_cal}, Median: {median_cal}, Std Dev: {std_cal}")

B. Grouping by Age for Water Intake
# Create Age Bins
bins = [18, 30, 45, 60, 100]
labels = ['18-30', '31-45', '46-60', '61+']
df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=labels)

# Pivot Table for Average Water Intake
water_pivot = df.pivot_table(values='Water Intake (Liters)', index='Age Group', aggfunc='mean')
water_pivot.plot(kind='bar', color='teal', title='Average Water Intake by Age Group')
