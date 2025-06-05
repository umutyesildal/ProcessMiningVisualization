import pandas as pd

# Load processed Road Traffic Fines event log
df = pd.read_csv('processed_trafficfines.csv')

# Group by event type and calculate descriptive stats
summary = df.groupby('concept:name')['time_since_case_start'].describe(percentiles=[0.25, 0.5, 0.75])
print(summary[['min', '25%', '50%', '75%', 'max', 'count']])

# Save to CSV for manual inspection
summary[['min', '25%', '50%', '75%', 'max', 'count']].to_csv('trafficfines_event_type_time_stats.csv')
print('Saved trafficfines_event_type_time_stats.csv')
