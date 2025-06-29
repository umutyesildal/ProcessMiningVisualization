import pandas as pd

# Load the processed event log
df = pd.read_csv('processed_bpi2017.csv')

# Group by event type and calculate head (min), median, and count
grouped = df.groupby('concept:name')['time_since_case_start']
stats = grouped.agg(['min', 'median', 'count'])
stats = stats.rename(columns={'min': 'head', 'median': 'median', 'count': 'count'})

# Print to console
print(stats)

# Save to CSV for manual inspection
stats.to_csv('event_type_head_median.csv')
print('Saved event_type_head_median.csv')
