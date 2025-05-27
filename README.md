# ProcessMiningVisualization

A Python Dash web application for interactive visualization of event log data (e.g., BPI Challenge 2017) using violin plots.

## Features
- Load and preprocess XES event log files (with PM4Py)
- Visualize event type distributions over time with violin plots (Plotly)
- Interactive sorting by statistical parameters (min, max, mean, median, quartiles)
- Log transformation for better visualization of skewed data
- Loader spinner for user feedback

## Quickstart

1. **Clone the repository:**
   ```bash
   git clone https://github.com/umutyesildal/ProcessMiningVisualization.git
   cd ProcessMiningVisualization
   ```
2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   # or manually:
   pip install pandas numpy plotly dash pm4py
   ```
4. **Add your XES file** (e.g., `BPI Challenge 2017.xes`) to the project directory.
5. **Preprocess the data:**
   ```bash
   python data_processing.py
   ```
6. **Run the Dash app:**
   ```bash
   python app.py
   ```
7. **Open your browser:**
   Go to [http://127.0.0.1:8050](http://127.0.0.1:8050)

## File Structure
```
ProcessMiningVisualization/
├── app.py                # Dash web app
├── data_processing.py    # Data preprocessing script
├── .gitignore
├── README.md
└── ...
```

## Notes
- The `.gitignore` excludes large data files and virtual environments.
- For large datasets, log transformation and outlier handling are recommended for meaningful violin plots.

## License
This project is for academic/research use. See repository for details.
