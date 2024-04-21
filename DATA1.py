import pandas as pd

file_path = "Desktop\jahs.csv"  
data = pd.read_csv(file_path)

print("First few rows of the dataset:")
print(data.head())

print("\nDataset shape:", data.shape)

print("\nMissing values:")
print(data.isnull().sum())

print("\nSummary statistics:")
print(data.describe())

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.plot(data['Year'], data['Unemployment Rate'], marker='o', linestyle='-')
plt.title('Unemployment Rate in India Over Time')
plt.xlabel('Year')
plt.ylabel('Unemployment Rate (%)')
plt.grid(True)
plt.show()
