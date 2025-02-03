import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("athelete_events.csv")

# Print first 5 rows
print(df.head())

# Plot a histogram of ages
plt.figure(figsize=(10, 5))
df['Age'].dropna().hist(bins=20)
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Distribution of Athletes' Ages")

# Save the figure to src folder
plt.savefig("src/age_distribution.png")
print("Figure saved as src/age_distribution.png")