import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a pandas DataFrame
# Make sure to replace 'your_data.csv' with the actual name of your file
df = pd.read_csv('calculation_AAPL.csv')

# Convert the 'Date' column to datetime objects
df['Date'] = pd.to_datetime(df['Date'])

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Daily_Returns'], marker='o', linestyle='-')

# Add titles and labels for clarity
plt.title('Daily Returns Over Time')
plt.xlabel('Date')
plt.ylabel('Daily Returns')
plt.grid(True)

# Rotate date labels for better readability
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot to a file
plt.savefig('daily_returns_plot.png')

print("Plot saved as daily_returns_plot.png")
