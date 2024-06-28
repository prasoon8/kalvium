import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the data from the CSV file
df = pd.read_csv('party_data.csv')

# Display the first few rows of the DataFrame
print(df.head())

# Adding a log scale column for better visualization
df['LogTotal'] = np.log1p(df['Total'])
df['LogWon'] = np.log1p(df['Won'])

# Visualizations

# 1. Total seats won by each party (log scale)
plt.figure(figsize=(14, 7))
sns.barplot(data=df, x='LogTotal', y='Party', palette='viridis')
plt.title('Total Seats Won by Each Party (Log Scale)')
plt.xlabel('Log of Total Seats')
plt.ylabel('Party')
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)  # Reduce y-axis label size
plt.tight_layout()  # Adjust the layout to ensure y-axis labels are not cut off
plt.show()

# 2. Comparison of seats won (log scale)
plt.figure(figsize=(14, 7))
sns.barplot(data=df, x='LogWon', y='Party', palette='coolwarm')
plt.title('Comparison of Seats Won by Each Party (Log Scale)')
plt.xlabel('Log of Seats Won')
plt.ylabel('Party')
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)  # Reduce y-axis label size
plt.tight_layout()  # Adjust the layout to ensure y-axis labels are not cut off
plt.show()

# 3. Distribution of seats won (log scale)
plt.figure(figsize=(14, 7))
sns.boxplot(data=df, x='LogWon', palette='magma')
plt.title('Distribution of Seats Won by Each Party (Log Scale)')
plt.xlabel('Log of Seats Won')
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)  # Reduce y-axis label size
plt.tight_layout()  # Adjust the layout to ensure y-axis labels are not cut off
plt.show()
