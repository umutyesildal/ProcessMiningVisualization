# Process Mining Violin Plot Visualization

A simple Dash web application for visualizing event log temporal patterns using violin plots.

## Overview

This project creates interactive violin plot visualizations for process mining event logs, specifically focused on the **Road Traffic Fines Management Process** dataset.

## Features

- **Simple violin plots** showing event duration distributions
- **Log-transformed time data** for better visualization
- **Top event types** filtering for clean charts
- **Interactive web interface** using Dash/Plotly

## Quick Start

1. **Activate virtual environment:**
```bash
source venv/bin/activate
```

2. **Run the app:**
```bash
python app.py
```

3. **Open in browser:**
```
http://127.0.0.1:8050
```

## Files

- `app.py` - Main Dash application
- `data_processing.py` - XES to CSV conversion
- `processed_trafficfines.csv` - Processed traffic fines data
- `Road_Traffic_Fine_Management_Process.xes` - Original XES log

## Data Processing

The app uses pre-processed traffic fines data with:
- **Time since case start** calculated in hours
- **Log transformation** applied for better distribution visibility
- **Top 4 event types** selected for clean visualization

## Dependencies

- pandas
- plotly
- dash
- pm4py
- numpy
