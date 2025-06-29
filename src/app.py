# -*- coding: utf-8 -*-
import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html, Input, Output
import numpy as np
import os
import sys

# Add utils to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))
from transformations import transform_time_data, get_transformation_options

# Dataset Configuration
DATASETS = {
    'traffic_fines': {
        'name': '🚗 Traffic Fines',
        'file': 'processed_road_traffic_fine_management_process.csv',
        'description': 'Road Traffic Fine Management Process',
        'domain': 'Government',
        'cases': '150,370',
        'events': '561,470'
    },
    'bpi_2012': {
        'name': '🏦 BPI Challenge 2012',
        'file': 'processed_bpi_challenge_2012.csv',
        'description': 'Loan Application Process',
        'domain': 'Finance',
        'cases': '13,087',
        'events': '262,000'
    },
    'bpi_2017': {
        'name': '🏦 BPI Challenge 2017',
        'file': 'processed_bpi_challenge_2017.csv',
        'description': 'Credit Application Process',
        'domain': 'Finance',
        'cases': '31,509',
        'events': '1,202,267'
    },
    'sepsis': {
        'name': '🏥 Sepsis Cases',
        'file': 'processed_sepsis_cases___event_log.csv',
        'description': 'Hospital Patient Treatment Process',
        'domain': 'Healthcare',
        'cases': '1,050',
        'events': '15,214'
    }
}

def load_dataset(dataset_key, num_events=6):
    """Load and process a dataset by key."""
    if dataset_key not in DATASETS:
        raise ValueError(f"Dataset {dataset_key} not found")
    
    dataset_info = DATASETS[dataset_key]
    data_path = os.path.join(os.path.dirname(__file__), '..', 'datasets', 'processed', dataset_info['file'])
    
    try:
        df = pd.read_csv(data_path)
        
        # Filter out the first events (time_since_case_start = 0) for meaningful temporal insights
        df_filtered = df[df['time_since_case_start'] > 0].copy()
        
        # Get top event types for filtering (from non-zero time events)
        top_events = df_filtered['concept:name'].value_counts().head(num_events).index.tolist()
        
        return df_filtered, top_events, dataset_info
        
    except Exception as e:
        print(f"Error loading dataset {dataset_key}: {e}")
        return None, None, None

# Create Dash app
app = dash.Dash(__name__, external_stylesheets=[
    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css'
])

# Add custom CSS
app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>Process Mining Violin Plot Dashboard</title>
        {%favicon%}
        {%css%}
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
            
            body {
                font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
                margin: 0;
                padding: 0;
            }
            
            /* Custom dropdown styling */
            .Select-control {
                border-radius: 10px !important;
                border: 2px solid #e0e0e0 !important;
                box-shadow: 0 2px 8px rgba(0,0,0,0.1) !important;
                transition: all 0.3s ease !important;
            }
            
            .Select-control:hover {
                border-color: #3498db !important;
                box-shadow: 0 4px 12px rgba(52, 152, 219, 0.2) !important;
            }
            
            .is-focused .Select-control {
                border-color: #3498db !important;
                box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.1) !important;
            }
            
            /* Tablet responsive design */
            @media (min-width: 769px) and (max-width: 1024px) {
                .sidebar {
                    width: 260px !important;
                }
                
                .main-chart {
                    margin-left: 280px !important;
                }
                
                .header-title {
                    font-size: 1.8rem !important;
                }
                
                .control-card {
                    padding: 12px !important;
                    margin-bottom: 12px !important;
                }
                
                .info-panel {
                    padding: 12px !important;
                }
            }

            /* Mobile responsive design */
            @media (max-width: 768px) {
                body {
                    font-size: 14px !important;
                }
                
                .sidebar {
                    position: relative !important;
                    width: 100% !important;
                    height: auto !important;
                    padding: 0 15px !important;
                    margin-bottom: 15px !important;
                    overflow-y: visible !important;
                }
                
                .main-chart {
                    margin-left: 0 !important;
                    margin-right: 0 !important;
                    padding: 10px !important;
                }
                
                .main-content {
                    flex-direction: column !important;
                }
                
                .header-title {
                    font-size: 1.5rem !important;
                    padding: 15px 10px 5px 10px !important;
                }
                
                .header-subtitle {
                    font-size: 0.9rem !important;
                    padding: 0 10px 15px 10px !important;
                }
                
                .control-card {
                    margin-bottom: 12px !important;
                    padding: 12px !important;
                    border-radius: 10px !important;
                }
                
                .info-panel {
                    padding: 12px !important;
                    margin-bottom: 12px !important;
                }
                
                .chart-container {
                    height: 400px !important;
                    margin: 0 !important;
                }
                
                /* Optimize dropdown for mobile */
                .Select-control {
                    border-radius: 8px !important;
                    padding: 2px !important;
                    font-size: 0.9rem !important;
                }
                
                .Select-menu-outer {
                    font-size: 0.9rem !important;
                }
            }
            
            /* Small mobile devices */
            @media (max-width: 480px) {
                .header-title {
                    font-size: 1.3rem !important;
                    padding: 10px 5px 5px 5px !important;
                }
                
                .header-subtitle {
                    font-size: 0.8rem !important;
                    padding: 0 5px 10px 5px !important;
                    margin-bottom: 0 !important;
                }
                
                .sidebar {
                    padding: 0 10px !important;
                }
                
                .main-chart {
                    padding: 8px !important;
                }
                
                .control-card {
                    padding: 10px !important;
                    margin-bottom: 10px !important;
                }
                
                .info-panel {
                    padding: 10px !important;
                }
                
                .chart-container {
                    height: 350px !important;
                }
                
                /* Better touch targets for mobile */
                .Select-control {
                    min-height: 44px !important;
                    font-size: 0.85rem !important;
                }
                
                .Select-arrow-zone {
                    width: 30px !important;
                }
            }
            
            /* Landscape mobile optimization */
            @media (max-width: 768px) and (orientation: landscape) {
                .chart-container {
                    height: 300px !important;
                }
                
                .control-card {
                    padding: 8px !important;
                    margin-bottom: 8px !important;
                }
                
                .info-panel {
                    padding: 8px !important;
                }
            }
        </style>
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

# Define custom styles
COLORS = {
    'background': '#f8f9fa',
    'card': '#ffffff',
    'primary': '#2c3e50',
    'secondary': '#3498db',
    'accent': '#e74c3c',
    'text': '#2c3e50',
    'text_light': '#7f8c8d',
    'border': '#bdc3c7'
}

app.layout = html.Div([
    # Header section - compact
    html.Div([
        html.H1(
            "🎻 Process Mining Violin Plot Dashboard", 
            className="header-title",
            style={
                'textAlign': 'center', 
                'color': COLORS['primary'],
                'fontSize': '2rem',
                'fontWeight': '700',
                'marginBottom': '5px',
                'fontFamily': 'Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif'
            }
        ),
        html.P(
            "Interactive visualization of temporal event distributions across multiple datasets",
            className="header-subtitle",
            style={
                'textAlign': 'center',
                'color': COLORS['text_light'],
                'fontSize': '1rem',
                'marginBottom': '0px',
                'fontFamily': 'Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif'
            }
        )
    ], style={
        'background': f'linear-gradient(135deg, {COLORS["card"]} 0%, #ecf0f1 100%)',
        'padding': '20px',
        'marginBottom': '10px',
        'borderRadius': '0 0 15px 15px',
        'boxShadow': '0 2px 10px rgba(0,0,0,0.08)'
    }),
    
    # Main content area - 2 column layout
    html.Div([
        # Left sidebar with controls
        html.Div([
            # Dataset selector - moved to sidebar
            html.Div([
                html.Div([
                    html.I(className="fas fa-database", style={'marginRight': '8px', 'color': COLORS['secondary']}),
                    html.Label(
                        "Dataset", 
                        style={
                            'fontWeight': '600', 
                            'marginBottom': '10px',
                            'color': COLORS['primary'],
                            'fontSize': '0.9rem',
                            'fontFamily': 'Inter, sans-serif'
                        }
                    )
                ], style={'display': 'flex', 'alignItems': 'center', 'marginBottom': '10px'}),
                
                dcc.Dropdown(
                    id='dataset-dropdown',
                    options=[
                        {'label': info['name'], 'value': key} 
                        for key, info in DATASETS.items()
                    ],
                    value='traffic_fines',
                    style={
                        'fontFamily': 'Inter, sans-serif',
                        'fontSize': '0.85rem'
                    }
                )
            ], className="control-card", style={
                'background': COLORS['card'],
                'padding': '15px',
                'borderRadius': '12px',
                'boxShadow': '0 3px 15px rgba(0,0,0,0.08)',
                'border': f'1px solid {COLORS["border"]}',
                'marginBottom': '15px'
            }),
            
            # Time transformation toggle buttons
            html.Div([
                html.Div([
                    html.I(className="fas fa-clock", style={'marginRight': '8px', 'color': COLORS['secondary']}),
                    html.Label(
                        "Time Transformation", 
                        style={
                            'fontWeight': '600', 
                            'marginBottom': '10px',
                            'color': COLORS['primary'],
                            'fontSize': '0.9rem',
                            'fontFamily': 'Inter, sans-serif'
                        }
                    )
                ], style={'display': 'flex', 'alignItems': 'center', 'marginBottom': '10px'}),
                
                # Transformation method dropdown
                dcc.Dropdown(
                    id='transformation-dropdown',
                    options=get_transformation_options(),
                    value='log_hours',
                    style={
                        'fontFamily': 'Inter, sans-serif',
                        'fontSize': '0.85rem'
                    }
                )
            ], className="control-card", style={
                'background': COLORS['card'],
                'padding': '15px',
                'borderRadius': '12px',
                'boxShadow': '0 3px 15px rgba(0,0,0,0.08)',
                'border': f'1px solid {COLORS["border"]}',
                'marginBottom': '15px'
            }),
            
            # Event sorting dropdown
            html.Div([
                html.Div([
                    html.I(className="fas fa-sort-amount-down", style={'marginRight': '8px', 'color': COLORS['secondary']}),
                    html.Label(
                        "Sort Events By", 
                        style={
                            'fontWeight': '600', 
                            'marginBottom': '10px',
                            'color': COLORS['primary'],
                            'fontSize': '0.9rem',
                            'fontFamily': 'Inter, sans-serif'
                        }
                    )
                ], style={'display': 'flex', 'alignItems': 'center', 'marginBottom': '10px'}),
                dcc.Dropdown(
                    id='sorting-dropdown',
                    options=[
                        {'label': '🔢 Most Frequent', 'value': 'frequency'},
                        {'label': '📊 Mean Time', 'value': 'mean'},
                        {'label': '📍 Median Time', 'value': 'median'},
                        {'label': '⬇️ Min Time', 'value': 'min'},
                        {'label': '⬆️ Max Time', 'value': 'max'},
                        {'label': '📈 25th Percentile', 'value': 'q1'},
                        {'label': '📈 75th Percentile', 'value': 'q3'}
                    ],
                    value='frequency',
                    style={
                        'fontFamily': 'Inter, sans-serif',
                        'fontSize': '0.85rem'
                    }
                )
            ], className="control-card", style={
                'background': COLORS['card'],
                'padding': '15px',
                'borderRadius': '12px',
                'boxShadow': '0 3px 15px rgba(0,0,0,0.08)',
                'border': f'1px solid {COLORS["border"]}',
                'marginBottom': '15px'
            }),
            
            # Number of events selector
            html.Div([
                html.Div([
                    html.I(className="fas fa-list-ol", style={'marginRight': '8px', 'color': COLORS['secondary']}),
                    html.Label(
                        "Events Count", 
                        style={
                            'fontWeight': '600', 
                            'marginBottom': '10px',
                            'color': COLORS['primary'],
                            'fontSize': '0.9rem',
                            'fontFamily': 'Inter, sans-serif'
                        }
                    )
                ], style={'display': 'flex', 'alignItems': 'center', 'marginBottom': '10px'}),
                dcc.Dropdown(
                    id='num-events-dropdown',
                    options=[
                        {'label': 'Top 4', 'value': 4},
                        {'label': 'Top 6', 'value': 6},
                        {'label': 'Top 8', 'value': 8},
                        {'label': 'Top 10', 'value': 10}
                    ],
                    value=6,
                    style={
                        'fontFamily': 'Inter, sans-serif',
                        'fontSize': '0.85rem'
                    }
                )
            ], className="control-card", style={
                'background': COLORS['card'],
                'padding': '15px',
                'borderRadius': '12px',
                'boxShadow': '0 3px 15px rgba(0,0,0,0.08)',
                'border': f'1px solid {COLORS["border"]}',
                'marginBottom': '15px'
            }),
            
            # Info panel - dynamic and compact
            html.Div([
                html.Div([
                    html.I(className="fas fa-info-circle", style={'marginRight': '8px', 'color': COLORS['secondary']}),
                    html.Label(
                        "Current Dataset", 
                        style={
                            'fontWeight': '600', 
                            'marginBottom': '10px',
                            'color': COLORS['primary'],
                            'fontSize': '0.9rem',
                            'fontFamily': 'Inter, sans-serif'
                        }
                    )
                ], style={'display': 'flex', 'alignItems': 'center', 'marginBottom': '10px'}),
                html.Div(id='dynamic-info-panel')
            ], className="info-panel", style={
                'background': f'linear-gradient(135deg, #e8f4fd 0%, #f8f9fa 100%)',
                'padding': '15px',
                'borderRadius': '12px',
                'border': f'2px dashed {COLORS["secondary"]}',
                'marginBottom': '15px'
            })
            
        ], className="sidebar", style={
            'width': '300px',
            'padding': '0 15px',
            'position': 'fixed',
            'height': 'calc(100vh - 120px)',
            'overflowY': 'auto',
            'overflowX': 'hidden'
        }),
        
        # Main chart area - stretched to the right
        html.Div([
            dcc.Graph(
                id='violin-plot',
                className="chart-container",
                style={
                    'height': 'calc(100vh - 160px)',
                    'background': COLORS['card'],
                    'borderRadius': '15px'
                }
            )
        ], className="main-chart", style={
            'background': COLORS['card'],
            'marginLeft': '330px',
            'marginRight': '10px',
            'padding': '15px',
            'borderRadius': '15px',
            'boxShadow': '0 4px 25px rgba(0,0,0,0.1)',
            'border': f'1px solid {COLORS["border"]}'
        })
        
    ], className="main-content", style={'minHeight': 'calc(100vh - 80px)'})
    
], style={
    'background': COLORS['background'],
    'minHeight': '100vh',
    'fontFamily': 'Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif'
})

# Callback to update dataset info display in sidebar
@app.callback(
    Output('dynamic-info-panel', 'children'),
    [Input('dataset-dropdown', 'value'),
     Input('num-events-dropdown', 'value')]
)
def update_dataset_info(selected_dataset, num_events):
    if selected_dataset not in DATASETS:
        return html.P("Error", style={'color': 'red'})
    
    dataset_info = DATASETS[selected_dataset]
    
    # Compact sidebar info panel
    sidebar_info = html.Div([
        html.P(f"{dataset_info['name']}", style={
            'margin': '3px 0', 
            'fontSize': '0.8rem', 
            'color': COLORS['text'],
            'fontWeight': '600'
        }),
        html.P(f"🏢 {dataset_info['domain']}", style={
            'margin': '3px 0', 
            'fontSize': '0.75rem', 
            'color': COLORS['text_light']
        }),
        html.P(f"📊 {dataset_info['cases']} cases", style={
            'margin': '3px 0', 
            'fontSize': '0.75rem', 
            'color': COLORS['text_light']
        }),
        html.P("🧹 Case-start events excluded", style={
            'margin': '3px 0', 
            'fontSize': '0.75rem', 
            'color': COLORS['text']
        }),
        html.P(f"📈 Top {num_events} event types", style={
            'margin': '3px 0', 
            'fontSize': '0.75rem', 
            'color': COLORS['text']
        })
    ])
    
    return sidebar_info

# Callback to update the violin plot based on selected dataset, transformation, and sorting
@app.callback(
    Output('violin-plot', 'figure'),
    [Input('dataset-dropdown', 'value'),
     Input('transformation-dropdown', 'value'),
     Input('sorting-dropdown', 'value'),
     Input('num-events-dropdown', 'value')]
)
def update_violin_plot(selected_dataset, transformation, sorting, num_events):
    # Load the selected dataset
    df_filtered_time, top_events, dataset_info = load_dataset(selected_dataset, num_events)
    
    if df_filtered_time is None:
        # Return empty figure if dataset loading fails
        return px.scatter(title="Error loading dataset")
    
    # Filter to top N event types for better visualization
    df_final = df_filtered_time[df_filtered_time['concept:name'].isin(top_events)].copy()
    
    # Apply the selected transformation using the transformations module
    transformed_data, x_title, plot_title = transform_time_data(
        df_final['time_since_case_start'], 
        transformation
    )
    df_final.loc[:, 'transformed_time'] = transformed_data
    
    # Update plot title to include dataset name
    plot_title = f"{plot_title} - {dataset_info['name']}"
    
    # Calculate statistics for sorting
    if sorting == 'frequency':
        # Sort by frequency (most common first)
        event_order = df_final['concept:name'].value_counts().index.tolist()
    else:
        # Calculate statistics for each event type
        stats_df = df_final.groupby('concept:name')['transformed_time'].agg([
            'mean', 'median', 'min', 'max',
            lambda x: x.quantile(0.25),  # Q1
            lambda x: x.quantile(0.75)   # Q3
        ]).reset_index()
        
        stats_df.columns = ['concept:name', 'mean', 'median', 'min', 'max', 'q1', 'q3']
        
        # Sort based on selected metric
        if sorting == 'mean':
            stats_df = stats_df.sort_values('mean', ascending=True)
        elif sorting == 'median':
            stats_df = stats_df.sort_values('median', ascending=True)
        elif sorting == 'min':
            stats_df = stats_df.sort_values('min', ascending=True)
        elif sorting == 'max':
            stats_df = stats_df.sort_values('max', ascending=True)
        elif sorting == 'q1':
            stats_df = stats_df.sort_values('q1', ascending=True)
        elif sorting == 'q3':
            stats_df = stats_df.sort_values('q3', ascending=True)
        
        event_order = stats_df['concept:name'].tolist()
    
    # Dynamic color sequence based on number of events
    colors = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12', '#9b59b6', '#f1c40f', '#e67e22', '#1abc9c', '#34495e', '#95a5a6']
    color_sequence = colors[:num_events]
    
    # Create violin plot with custom ordering
    fig = px.violin(
        df_final, 
        x='transformed_time', 
        y='concept:name',
        orientation='h',
        box=True,
        title=plot_title,
        category_orders={'concept:name': event_order},
        color_discrete_sequence=color_sequence
    )
    
    fig.update_layout(
        title={
            'text': plot_title,
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18, 'color': COLORS['primary'], 'family': 'Inter, Arial, sans-serif'}
        },
        xaxis_title=x_title,
        yaxis_title="Event Type",
        font={'family': 'Inter, Arial, sans-serif', 'color': COLORS['text']},
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin={'t': 60, 'l': 200, 'r': 20, 'b': 60},
        xaxis={
            'gridcolor': '#f1f3f4',
            'linecolor': '#bdc3c7',
            'title_font': {'size': 12, 'color': COLORS['primary']},
            'tickfont': {'color': COLORS['text'], 'size': 10}
        },
        yaxis={
            'gridcolor': '#f1f3f4',
            'linecolor': '#bdc3c7',
            'title_font': {'size': 12, 'color': COLORS['primary']},
            'tickfont': {'color': COLORS['text'], 'size': 10}
        }
    )
    
    return fig

if __name__ == '__main__':
    app.run(debug=True)
