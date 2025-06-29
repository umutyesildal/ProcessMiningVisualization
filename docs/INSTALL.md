# Installation Guide

## Quick Setup

### 1. Clone the Repository
```bash
git clone https://github.com/umutyesildal/ProcessMiningVisualization.git
cd ProcessMiningVisualization
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Dashboard
```bash
python run_dashboard.py
```

### 5. Access the Dashboard
Open your browser and go to: `http://127.0.0.1:8050`

## Development Setup

For development work:

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run in development mode
cd src
python app.py
```

## Troubleshooting

### Common Issues

1. **Import Errors**: Make sure virtual environment is activated
2. **Data Not Found**: Ensure datasets are in `datasets/processed/` folder
3. **Port Issues**: Check if port 8050 is available

### System Requirements

- Python 3.8 or higher
- 4GB RAM minimum
- Modern web browser (Chrome, Firefox, Safari, Edge)
