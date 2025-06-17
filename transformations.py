"""
Time Transformation Methods for Process Mining Visualization

This module contains various time transformation methods used to preprocess
event log time data for better visualization in violin plots.
"""

import numpy as np
from sklearn.preprocessing import MinMaxScaler


def transform_time_data(data, transformation_type):
    """
    Apply the specified transformation to time data.
    
    Args:
        data (pd.Series): Time since case start in hours
        transformation_type (str): Type of transformation to apply
        
    Returns:
        tuple: (transformed_data, x_axis_title, plot_title)
    """
    
    if transformation_type == 'raw_hours':
        transformed_data = data
        x_title = "Time Since Case Start (Hours)"
        plot_title = "🕐 Event Time Distribution - Raw Time (Hours)"
        
    elif transformation_type == 'raw_days':
        transformed_data = data / 24
        x_title = "Time Since Case Start (Days)"
        plot_title = "📅 Event Time Distribution - Raw Time (Days)"
        
    elif transformation_type == 'raw_weeks':
        transformed_data = np.round(data / (24 * 7), 1)  # Round to 1 decimal place
        x_title = "Time Since Case Start (Weeks)"
        plot_title = "📊 Event Time Distribution - Raw Time (Weeks)"
        
    elif transformation_type == 'raw_months':
        # Convert to months and round to whole numbers
        transformed_data = np.round(data / (24 * 30.44), 0)  # Round to whole months
        x_title = "Time Since Case Start (Months)"
        plot_title = "📆 Event Time Distribution - Raw Time (Months)"
        
    elif transformation_type == 'sqrt_hours':
        transformed_data = np.sqrt(data)
        x_title = "√(Time Since Case Start) (√Hours)"
        plot_title = "√ Event Time Distribution - Square Root Time"
        
    elif transformation_type == 'minmax':
        scaler = MinMaxScaler()
        transformed_data = scaler.fit_transform(data.values.reshape(-1, 1)).flatten()
        x_title = "Min-Max Scaled Time (0-1)"
        plot_title = "📏 Event Time Distribution - Min-Max Scaled"
        
    else:  # log_hours (default)
        transformed_data = np.log1p(data)
        x_title = "Log(Time Since Case Start + 1)"
        plot_title = "📊 Event Time Distribution - Log Time"
    
    return transformed_data, x_title, plot_title


def get_transformation_options():
    """
    Get the available transformation options for the dropdown.
    
    Returns:
        list: List of transformation options with labels and values
    """
    return [
        {'label': '📊 Log Time (Hours)', 'value': 'log_hours'},
        {'label': '🕐 Raw Time (Hours)', 'value': 'raw_hours'},
        {'label': '📅 Raw Time (Days)', 'value': 'raw_days'},
        {'label': '📊 Raw Time (Weeks)', 'value': 'raw_weeks'},
        {'label': '📆 Raw Time (Months)', 'value': 'raw_months'},
        {'label': '√ Square Root (Hours)', 'value': 'sqrt_hours'},
        {'label': '📏 Min-Max Scaled', 'value': 'minmax'}
    ]


# Transformation descriptions for documentation
TRANSFORMATION_DESCRIPTIONS = {
    'log_hours': {
        'name': 'Logarithmic Transformation',
        'description': 'Applies log(x + 1) to compress large values and spread small values. Best for highly skewed data.',
        'use_case': 'When most events happen early but some occur much later (common in process mining)',
        'formula': 'log(hours + 1)'
    },
    'raw_hours': {
        'name': 'Raw Hours',
        'description': 'Original time data in hours since case start. Shows absolute time differences.',
        'use_case': 'When you want to see actual time durations without transformation',
        'formula': 'hours'
    },
    'raw_days': {
        'name': 'Raw Days',
        'description': 'Time converted to days since case start for longer processes.',
        'use_case': 'For processes that typically span multiple days',
        'formula': 'hours / 24'
    },
    'raw_weeks': {
        'name': 'Raw Weeks',
        'description': 'Time converted to weeks, rounded to one decimal place for readability.',
        'use_case': 'For long-running processes spanning weeks or months',
        'formula': 'round(hours / (24 * 7), 1)'
    },
    'raw_months': {
        'name': 'Raw Months',
        'description': 'Time converted to whole months for very long processes.',
        'use_case': 'For processes that can span many months (e.g., legal cases, long-term projects)',
        'formula': 'round(hours / (24 * 30.44), 0)'
    },
    'sqrt_hours': {
        'name': 'Square Root Transformation',
        'description': 'Applies square root to reduce the impact of outliers while preserving data shape.',
        'use_case': 'When data is moderately skewed and you want gentler compression than log',
        'formula': '√hours'
    },
    'minmax': {
        'name': 'Min-Max Scaling',
        'description': 'Scales all values to range 0-1, preserving relative relationships.',
        'use_case': 'For comparing patterns across different time scales or normalizing data',
        'formula': '(x - min) / (max - min)'
    }
}
