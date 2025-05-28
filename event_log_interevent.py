import pandas as pd
import numpy as np

# Load the processed event log
df = pd.read_csv('processed_bpi2017.csv')

# Sort by case and timestamp to compute inter-event times
# Ensure timestamp is in datetime format
if not np.issubdtype(df['time:timestamp'].dtype, np.datetime64):
    df['time:timestamp'] = pd.to_datetime(df['time:timestamp'], format='ISO8601')

df = df.sort_values(['case:concept:name', 'time:timestamp'])

# Compute inter-event time (in hours) within each case
df['inter_event_time'] = df.groupby('case:concept:name')['time:timestamp'].diff().dt.total_seconds() / 3600

# Remove the first event in each case (inter_event_time is NaN)
df_inter = df.dropna(subset=['inter_event_time'])

# Optionally filter out extreme outliers (e.g., above 99th percentile)
upper_limit = df_inter['inter_event_time'].quantile(0.99)
df_inter = df_inter[df_inter['inter_event_time'] <= upper_limit]

# Save for visualization or further analysis
df_inter.to_csv('processed_bpi2017_interevent.csv', index=False)
print('Saved processed_bpi2017_interevent.csv with inter-event times.')
