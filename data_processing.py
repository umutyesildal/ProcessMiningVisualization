import pm4py
import pandas as pd

def load_and_process_log(path):
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
    for xes_file, out_csv in [
        ("data/BPI_Challenge_2012.xes", "data/processed_bpi2012.csv"),
        ("data/Road_Traffic_Fine_Management_Process.xes", "data/processed_trafficfines.csv"),
        ("data/Sepsis Cases - Event Log.xes", "data/processed_sepsis.csv")
    ]:
        print(f"Processing {xes_file}...")
        df = load_and_process_log(xes_file)
        df.to_csv(out_csv, index=False)
        print(f"Saved {out_csv}")
