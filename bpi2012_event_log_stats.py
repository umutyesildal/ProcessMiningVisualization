import pandas as pd

# Load processed BPI 2012 event log
df = pd.read_csv('processed_bpi2012.csv')

# Group by event type and calculate descriptive stats
summary = df.groupby('concept:name')['time_since_case_start'].describe(percentiles=[0.25, 0.5, 0.75])
print(summary[['min', '25%', '50%', '75%', 'max', 'count']])

# Save to CSV for manual inspection
summary[['min', '25%', '50%', '75%', 'max', 'count']].to_csv('bpi2012_event_type_time_stats.csv')
print('Saved bpi2012_event_type_time_stats.csv')
