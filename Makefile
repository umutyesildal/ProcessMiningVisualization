# Process Mining Dashboard Makefile
# Provides convenient commands for common tasks

.PHONY: help install process run setup clean test

# Default target
help:
	@echo "Process Mining Dashboard - Available Commands:"
	@echo ""
	@echo "  make install     - Install dependencies"
	@echo "  make process     - Process XES files to CSV"
	@echo "  make run         - Run the dashboard"
	@echo "  make setup       - Full setup (install + process + run)"
	@echo "  make clean       - Clean temporary files"
	@echo "  make test        - Test the installation"
	@echo ""

# Install dependencies
install:
	@echo "Installing dependencies..."
	pip install -r requirements.txt

# Process XES files
process:
	@echo "Processing XES files..."
	python setup_and_run.py --process-data

# Run dashboard
run:
	@echo "Starting dashboard..."
	python setup_and_run.py --skip-processing

# Full setup and run
setup: install
	@echo "Full setup and run..."
	python setup_and_run.py

# Clean temporary files
clean:
	@echo "Cleaning temporary files..."
	find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
	find . -name "*.pyc" -delete
	find . -name "*.pyo" -delete
	find . -name ".DS_Store" -delete

# Test installation
test:
	@echo "Testing installation..."
	python -c "import pandas, plotly, dash, numpy, sklearn, pm4py; print('✅ All packages installed correctly')"
