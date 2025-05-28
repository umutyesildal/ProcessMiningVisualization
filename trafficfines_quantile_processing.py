import pandas as pd
import numpy as np

# Load processed Road Traffic Fines event log
df = pd.read_csv('processed_trafficfines.csv')

# Quantile clipping: remove top and bottom 1% for each event type
def quantile_clip(group):
    lower = group['time_since_case_start'].quantile(0.01)
    upper = group['time_since_case_start'].quantile(0.99)
    return group[(group['time_since_case_start'] >= lower) & (group['time_since_case_start'] <= upper)]

filtered = df.groupby('concept:name', group_keys=False).apply(quantile_clip)

# Add log-transformed and z-score normalized columns
filtered['log_time'] = np.log1p(filtered['time_since_case_start'])
filtered['zscore_time'] = filtered.groupby('concept:name')['time_since_case_start'].transform(lambda x: (x - x.mean()) / x.std())

filtered.to_csv('trafficfines_filtered_quantile.csv', index=False)
print('Saved trafficfines_filtered_quantile.csv with quantile clipping, log, and z-score columns.')

# --- Inter-event time processing ---
# Sort by case and timestamp
interevent = df.sort_values(['case:concept:name', 'time:timestamp']).copy()
# Compute inter-event time (in seconds) within each case
interevent['inter_event_time'] = interevent.groupby('case:concept:name')['time:timestamp'].transform(lambda x: pd.to_datetime(x).diff().dt.total_seconds())

# Remove first event in each case (no inter-event time)
interevent = interevent[~interevent['inter_event_time'].isna()]

# Quantile clipping for inter-event time per event type

def quantile_clip_interevent(group):
    lower = group['inter_event_time'].quantile(0.01)
    upper = group['inter_event_time'].quantile(0.99)
    return group[(group['inter_event_time'] >= lower) & (group['inter_event_time'] <= upper)]

filtered_interevent = interevent.groupby('concept:name', group_keys=False).apply(quantile_clip_interevent)

# Add log-transformed and z-score normalized columns for inter-event time
filtered_interevent['log_inter_event_time'] = np.log1p(filtered_interevent['inter_event_time'])
filtered_interevent['zscore_inter_event_time'] = filtered_interevent.groupby('concept:name')['inter_event_time'].transform(lambda x: (x - x.mean()) / x.std())

filtered_interevent.to_csv('trafficfines_interevent_quantile.csv', index=False)
print('Saved trafficfines_interevent_quantile.csv with inter-event time quantile clipping, log, and z-score columns.')
