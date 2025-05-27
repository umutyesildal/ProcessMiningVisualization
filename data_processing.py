import pm4py
import pandas as pd

def load_and_process_log(path='BPI Challenge 2017.xes'):
    # Load XES log
    log = pm4py.read_xes(path)
    
    # Convert to DataFrame
    df = pm4py.convert_to_dataframe(log)

    # Calculate time since case start (in hours)
    df['time_since_case_start'] = df.groupby('case:concept:name')['time:timestamp'].transform(
        lambda x: (x - x.min()).dt.total_seconds() / 3600
    )
    
    return df

if __name__ == "__main__":
    df = load_and_process_log()
    df.to_csv('processed_bpi2017.csv', index=False)
