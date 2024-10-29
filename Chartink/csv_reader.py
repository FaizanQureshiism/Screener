import csv
import numpy as np
import pandas as pd

# Assuming the CSV is loaded correctly
df = pd.read_csv('Backtest 1 Min Bull by DNM_OG, Technical Analysis Scanner.csv')

# Convert 'date' column to datetime and sort values
df["date"] = pd.to_datetime(df["date"])
df.sort_values(by='date', inplace=True)

# Create a pivot table, counting the number of 'symbol' per 'date'
table = df.pivot_table(df, index=['date'], columns=['symbol'], aggfunc='size', fill_value=0)

# Add a 'Total' column summing across symbols
table['Total'] = table.sum(axis=1)

# Filter only the 'date' and 'Total' columns
table_total = table[['Total']]

# Print the resulting table with only date and Total columns
print(table_total)

max_total = table_total['Total'].max()
print(f"Maximum Total: {max_total}")