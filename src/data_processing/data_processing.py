#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
XES to CSV Data Processing Module

This module provides functions to convert XES event logs to CSV format
with time-since-case-start calculations for process mining analysis.
"""

import pm4py
import pandas as pd
import os
from pathlib import Path

def process_xes_to_csv(xes_path, csv_path):
    """
    Convert XES event log to CSV with time calculations.
    
    Args:
        xes_path (str): Path to input XES file
        csv_path (str): Path to output CSV file
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        print(f"   Loading XES file: {xes_path}")
        
        # Load XES log
        log = pm4py.read_xes(xes_path)
        print(f"   Loaded {len(log)} cases")
        
        # Convert to DataFrame  
        df = pm4py.convert_to_dataframe(log)
        print(f"   Converted to DataFrame: {len(df)} events")
        
        # Calculate time since case start (in hours)
        df['time_since_case_start'] = df.groupby('case:concept:name')['time:timestamp'].transform(
            lambda x: (x - x.min()).dt.total_seconds() / 3600
        )
        
        # Sort by case and timestamp for consistency
        df = df.sort_values(['case:concept:name', 'time:timestamp'])
        
        # Save to CSV
        df.to_csv(csv_path, index=False)
        print(f"   Saved to: {csv_path}")
        
        return True
        
    except Exception as e:
        print(f"   Error processing {xes_path}: {e}")
        return False

def batch_process_directory(raw_dir, processed_dir):
    """
    Process all XES files in a directory.
    
    Args:
        raw_dir (str): Directory containing XES files
        processed_dir (str): Directory for output CSV files
        
    Returns:
        list: List of successfully processed files
    """
    raw_path = Path(raw_dir)
    processed_path = Path(processed_dir)
    
    # Create output directory
    processed_path.mkdir(parents=True, exist_ok=True)
    
    # Find XES files
    xes_files = list(raw_path.glob("*.xes"))
    successful = []
    
    for xes_file in xes_files:
        # Generate output filename
        csv_name = f"processed_{xes_file.stem.lower().replace(' ', '_').replace('-', '_')}.csv"
        csv_path = processed_path / csv_name
        
        if process_xes_to_csv(str(xes_file), str(csv_path)):
            successful.append(csv_name)
    
    return successful

if __name__ == "__main__":
    # Process datasets if run directly
    print("Processing XES files to CSV...")
    
    # Define paths
    base_dir = Path(__file__).parent.parent.parent
    raw_dir = base_dir / "datasets" / "raw"
    processed_dir = base_dir / "datasets" / "processed"
    
    # Process all files
    successful = batch_process_directory(str(raw_dir), str(processed_dir))
    
    print(f"Successfully processed {len(successful)} files:")
    for filename in successful:
        print(f"   • {filename}")
