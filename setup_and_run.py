#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Process Mining Dashboard - Complete Setup & Data Processing Pipeline

This script handles:
1. Data processing (XES to CSV conversion)
2. Environment validation
3. Dashboard launch

Usage:
    python setup_and_run.py [options]
    
Options:
    --process-data    Process all XES files to CSV
    --skip-processing Skip data processing, just run dashboard
    --help           Show this help message
"""

import sys
import os
import argparse
import subprocess
import glob
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def check_requirements():
    """Check if all required packages are installed."""
    try:
        import pandas
        import plotly
        import dash
        import numpy
        import sklearn
        import pm4py
        print("✅ All required packages are installed")
        return True
    except ImportError as e:
        print(f"❌ Missing required package: {e}")
        print("Please run: pip install -r requirements.txt")
        return False

def process_datasets():
    """Process all XES files in datasets/raw/ to CSV format."""
    print("🔄 Processing XES files to CSV...")
    
    raw_dir = Path("datasets/raw")
    processed_dir = Path("datasets/processed")
    
    # Ensure processed directory exists
    processed_dir.mkdir(parents=True, exist_ok=True)
    
    # Find all XES files
    xes_files = list(raw_dir.glob("*.xes"))
    
    if not xes_files:
        print("⚠️  No XES files found in datasets/raw/")
        return False
    
    # Import data processing module
    try:
        # Add src path and import
        src_path = os.path.join(os.path.dirname(__file__), 'src')
        if src_path not in sys.path:
            sys.path.insert(0, src_path)
        
        from data_processing.data_processing import process_xes_to_csv
        
        for xes_file in xes_files:
            print(f"   Processing: {xes_file.name}")
            
            # Generate output filename
            csv_name = f"processed_{xes_file.stem.lower().replace(' ', '_').replace('-', '_')}.csv"
            csv_path = processed_dir / csv_name
            
            try:
                # Process the file
                success = process_xes_to_csv(str(xes_file), str(csv_path))
                if success:
                    print(f"   ✅ Created: {csv_path.name}")
                else:
                    print(f"   ❌ Failed: {xes_file.name}")
            except Exception as e:
                print(f"   ❌ Error processing {xes_file.name}: {e}")
        
        print("📊 Data processing complete!")
        return True
        
    except ImportError:
        print("❌ Could not import data processing module")
        return False

def validate_datasets():
    """Check if processed datasets exist."""
    processed_dir = Path("datasets/processed")
    csv_files = list(processed_dir.glob("*.csv"))
    
    if not csv_files:
        print("⚠️  No processed CSV files found!")
        print("   Run with --process-data flag first")
        return False
    
    print(f"📁 Found {len(csv_files)} processed datasets:")
    for csv_file in csv_files:
        size = csv_file.stat().st_size / (1024 * 1024)  # MB
        print(f"   • {csv_file.name} ({size:.1f} MB)")
    
    return True

def run_dashboard():
    """Launch the dashboard application."""
    print("🚀 Launching Process Mining Dashboard...")
    print("📊 Dashboard will be available at: http://127.0.0.1:8050")
    print("🔄 Press Ctrl+C to stop the server")
    
    try:
        from app import app
        app.run(debug=True, host='127.0.0.1', port=8050)
    except Exception as e:
        print(f"❌ Failed to start dashboard: {e}")
        return False

def main():
    """Main execution function."""
    parser = argparse.ArgumentParser(
        description="Process Mining Dashboard Setup & Runner",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python setup_and_run.py                    # Complete setup and run dashboard
  python setup_and_run.py --skip-processing  # Skip data processing, just run dashboard
  python setup_and_run.py --process-data     # Only process data, don't run dashboard
        """
    )
    
    parser.add_argument('--process-data', action='store_true',
                       help='Process XES files and exit (don\'t run dashboard)')
    parser.add_argument('--skip-processing', action='store_true',
                       help='Skip data processing, just run dashboard')
    
    args = parser.parse_args()
    
    print("🎻 Process Mining Violin Plot Dashboard")
    print("=" * 50)
    
    # Check requirements
    if not check_requirements():
        return 1
    
    # Handle process-data-only mode
    if args.process_data:
        success = process_datasets()
        print(f"✅ Data processing {'completed' if success else 'failed'}")
        return 0 if success else 1
    
    # Normal flow: check/process data then run dashboard
    if not args.skip_processing:
        print("\n📊 Step 1: Data Processing")
        if not validate_datasets():
            print("Processing required datasets...")
            if not process_datasets():
                print("❌ Data processing failed")
                return 1
        else:
            print("✅ Datasets already processed")
    else:
        print("\n⏭️  Skipping data processing...")
    
    print("\n🚀 Step 2: Launching Dashboard")
    run_dashboard()
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
