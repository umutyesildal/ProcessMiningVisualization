# Developer Guide

## Project Structure

```
pmva_implementation/
├── 📁 src/                          # Source code
│   ├── app.py                       # Main dashboard application
│   ├── utils/                       # Utility modules
│   │   └── transformations.py      # Time transformation functions
│   └── data_processing/             # Data processing modules
│       └── data_processing.py       # XES to CSV conversion
├── 📁 datasets/                     # Data storage
│   ├── raw/                         # Original XES files
│   └── processed/                   # Processed CSV files
├── 📁 scripts/                      # Analysis and utility scripts
│   └── analysis/                    # Data analysis scripts
├── 📁 docs/                         # Documentation
│   ├── papers/                      # Research papers
│   ├── INSTALL.md                   # Installation guide
│   └── DEVELOPER.md                 # This file
├── 📁 venv/                         # Virtual environment
├── run_dashboard.py                 # Main application launcher
├── requirements.txt                 # Python dependencies
└── README.md                        # Main documentation
```

## Adding New Datasets

1. Place XES files in `datasets/raw/`
2. Process using `src/data_processing/data_processing.py`
3. Processed CSV files go to `datasets/processed/`
4. Update `src/app.py` to support dataset switching

## Adding New Transformations

1. Edit `src/utils/transformations.py`
2. Add new transformation function
3. Update `get_transformation_options()` function
4. Add documentation to the transformation

## Testing

Run the dashboard locally:
```bash
python run_dashboard.py
```

## Code Style

- Follow PEP 8 guidelines
- Use descriptive variable names
- Add docstrings to functions
- Comment complex logic
