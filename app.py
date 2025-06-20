import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html, Input, Output
import numpy as np

# Load processed traffic fines data
df = pd.read_csv('data/processed_trafficfines.csv')

# Get top 4 event types for filtering
top_events = df['concept:name'].value_counts().head(4).index.tolist()

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
        <title>Traffic Fines Process Mining Dashboard</title>
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
                    width: 240px !important;
                }
                
                .main-chart {
                    margin-left: 260px !important;
                }
                
                .header-title {
                    font-size: 1.8rem !important;
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
                    margin-bottom: 20px !important;
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
                    margin-bottom: 15px !important;
                    padding: 15px !important;
                    border-radius: 10px !important;
                }
                
                .info-panel {
                    display: none !important;
                }
                
                .toggle-buttons {
                    flex-direction: column !important;
                    gap: 10px !important;
                }
                
                .toggle-button {
                    width: 100% !important;
                    border-radius: 8px !important;
                    margin-bottom: 0 !important;
                    padding: 12px 16px !important;
                    font-size: 0.9rem !important;
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
                    padding: 5px !important;
                }
                
                .control-card {
                    padding: 12px !important;
                    margin-bottom: 10px !important;
                }
                
                .toggle-button {
                    padding: 10px 12px !important;
                    font-size: 0.8rem !important;
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
                    padding: 10px !important;
                }
                
                .toggle-buttons {
                    flex-direction: row !important;
                    gap: 5px !important;
                }
                
                .toggle-button {
                    width: 50% !important;
                    padding: 8px 12px !important;
                    font-size: 0.8rem !important;
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
            "🚗 Traffic Fines Process Mining Dashboard", 
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
            "Interactive violin plots of event time distributions",
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
        'marginBottom': '20px',
        'borderRadius': '0 0 15px 15px',
        'boxShadow': '0 2px 10px rgba(0,0,0,0.08)'
    }),
    
    # Main content area - 2 column layout
    html.Div([
        # Left sidebar with controls
        html.Div([
            # Time transformation toggle buttons
            html.Div([
                html.Div([
                    html.I(className="fas fa-clock", style={'marginRight': '8px', 'color': COLORS['secondary']}),
                    html.Label(
                        "Time Transformation", 
                        style={
                            'fontWeight': '600', 
                            'marginBottom': '15px',
                            'color': COLORS['primary'],
                            'fontSize': '0.9rem',
                            'fontFamily': 'Inter, sans-serif'
                        }
                    )
                ], style={'display': 'flex', 'alignItems': 'center', 'marginBottom': '15px'}),
                
                # Toggle buttons for time transformation
                html.Div([
                    html.Button(
                        [html.I(className="fas fa-chart-line", style={'marginRight': '8px'}), "Log Time"],
                        id='log-button',
                        className="toggle-button",
                        n_clicks=0,
                        style={
                            'background': COLORS['secondary'],
                            'color': 'white',
                            'border': 'none',
                            'padding': '12px 20px',
                            'borderRadius': '8px 0 0 8px',
                            'fontWeight': '600',
                            'fontSize': '0.85rem',
                            'fontFamily': 'Inter, sans-serif',
                            'cursor': 'pointer',
                            'transition': 'all 0.3s ease',
                            'boxShadow': '0 2px 8px rgba(52, 152, 219, 0.3)',
                            'width': '50%'
                        }
                    ),
                    html.Button(
                        [html.I(className="fas fa-clock", style={'marginRight': '8px'}), "Raw Time"],
                        id='raw-button',
                        className="toggle-button",
                        n_clicks=0,
                        style={
                            'background': '#ecf0f1',
                            'color': COLORS['text'],
                            'border': 'none',
                            'padding': '12px 20px',
                            'borderRadius': '0 8px 8px 0',
                            'fontWeight': '500',
                            'fontSize': '0.85rem',
                            'fontFamily': 'Inter, sans-serif',
                            'cursor': 'pointer',
                            'transition': 'all 0.3s ease',
                            'width': '50%'
                        }
                    )
                ], className="toggle-buttons", style={'display': 'flex', 'width': '100%'})
            ], className="control-card", style={
                'background': COLORS['card'],
                'padding': '20px',
                'borderRadius': '12px',
                'boxShadow': '0 3px 15px rgba(0,0,0,0.08)',
                'border': f'1px solid {COLORS["border"]}',
                'marginBottom': '20px'
            }),
            
            # Event sorting dropdown
            html.Div([
                html.Div([
                    html.I(className="fas fa-sort-amount-down", style={'marginRight': '8px', 'color': COLORS['secondary']}),
                    html.Label(
                        "Sort Events By", 
                        style={
                            'fontWeight': '600', 
                            'marginBottom': '15px',
                            'color': COLORS['primary'],
                            'fontSize': '0.9rem',
                            'fontFamily': 'Inter, sans-serif'
                        }
                    )
                ], style={'display': 'flex', 'alignItems': 'center', 'marginBottom': '15px'}),
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
                'padding': '20px',
                'borderRadius': '12px',
                'boxShadow': '0 3px 15px rgba(0,0,0,0.08)',
                'border': f'1px solid {COLORS["border"]}',
                'marginBottom': '20px'
            }),
            
            # Info panel
            html.Div([
                html.Div([
                    html.I(className="fas fa-info-circle", style={'marginRight': '8px', 'color': COLORS['secondary']}),
                    html.Label(
                        "Dataset Info", 
                        style={
                            'fontWeight': '600', 
                            'marginBottom': '15px',
                            'color': COLORS['primary'],
                            'fontSize': '0.9rem',
                            'fontFamily': 'Inter, sans-serif'
                        }
                    )
                ], style={'display': 'flex', 'alignItems': 'center', 'marginBottom': '15px'}),
                html.Div([
                    html.P("📁 Road Traffic Fines", style={'margin': '5px 0', 'fontSize': '0.8rem', 'color': COLORS['text']}),
                    html.P("📊 Top 4 Event Types", style={'margin': '5px 0', 'fontSize': '0.8rem', 'color': COLORS['text']}),
                    html.P("🎻 Horizontal Violin Plots", style={'margin': '5px 0', 'fontSize': '0.8rem', 'color': COLORS['text']}),
                    html.P("📦 Box plots included", style={'margin': '5px 0', 'fontSize': '0.8rem', 'color': COLORS['text']})
                ])
            ], className="info-panel", style={
                'background': f'linear-gradient(135deg, #e8f4fd 0%, #f8f9fa 100%)',
                'padding': '20px',
                'borderRadius': '12px',
                'border': f'2px dashed {COLORS["secondary"]}',
                'marginBottom': '20px'
            })
            
        ], className="sidebar", style={
            'width': '280px',
            'padding': '0 20px 0 20px',
            'position': 'fixed',
            'height': 'calc(100vh - 140px)',
            'overflowY': 'auto'
        }),
        
        # Main chart area - stretched to the right
        html.Div([
            dcc.Graph(
                id='violin-plot',
                className="chart-container",
                style={
                    'height': 'calc(100vh - 180px)',
                    'background': COLORS['card'],
                    'borderRadius': '15px'
                }
            )
        ], className="main-chart", style={
            'background': COLORS['card'],
            'marginLeft': '320px',
            'marginRight': '10px',
            'padding': '20px',
            'borderRadius': '15px',
            'boxShadow': '0 4px 25px rgba(0,0,0,0.1)',
            'border': f'1px solid {COLORS["border"]}'
        })
        
    ], className="main-content", style={'minHeight': 'calc(100vh - 100px)'}),
    
    # Hidden store for time transformation state
    dcc.Store(id='time-transformation-store', data='log')
    
], style={
    'background': COLORS['background'],
    'minHeight': '100vh',
    'fontFamily': 'Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif'
})

# Callback to handle button styling and time transformation state
@app.callback(
    [Output('log-button', 'style'),
     Output('raw-button', 'style'),
     Output('time-transformation-store', 'data')],
    [Input('log-button', 'n_clicks'),
     Input('raw-button', 'n_clicks')],
    prevent_initial_call=False
)
def update_button_styles(log_clicks, raw_clicks):
    ctx = dash.callback_context
    
    # Default to log transformation
    if not ctx.triggered:
        active_transformation = 'log'
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        if button_id == 'log-button':
            active_transformation = 'log'
        else:
            active_transformation = 'raw'
    
    # Active button style
    active_style = {
        'background': COLORS['secondary'],
        'color': 'white',
        'border': 'none',
        'padding': '12px 20px',
        'fontWeight': '600',
        'fontSize': '0.85rem',
        'fontFamily': 'Inter, sans-serif',
        'cursor': 'pointer',
        'transition': 'all 0.3s ease',
        'boxShadow': '0 2px 8px rgba(52, 152, 219, 0.3)',
        'width': '50%',
        'transform': 'translateY(-1px)'
    }
    
    # Inactive button style
    inactive_style = {
        'background': '#ecf0f1',
        'color': COLORS['text'],
        'border': 'none',
        'padding': '12px 20px',
        'fontWeight': '500',
        'fontSize': '0.85rem',
        'fontFamily': 'Inter, sans-serif',
        'cursor': 'pointer',
        'transition': 'all 0.3s ease',
        'width': '50%'
    }
    
    if active_transformation == 'log':
        log_style = {**active_style, 'borderRadius': '8px 0 0 8px'}
        raw_style = {**inactive_style, 'borderRadius': '0 8px 8px 0'}
    else:
        log_style = {**inactive_style, 'borderRadius': '8px 0 0 8px'}
        raw_style = {**active_style, 'borderRadius': '0 8px 8px 0'}
    
    return log_style, raw_style, active_transformation

# Callback to update the violin plot based on selected transformation and sorting
@app.callback(
    Output('violin-plot', 'figure'),
    [Input('time-transformation-store', 'data'),
     Input('sorting-dropdown', 'value')]
)
def update_violin_plot(transformation, sorting):
    # Filter data to top 4 event types (create a proper copy)
    df_filtered = df[df['concept:name'].isin(top_events)].copy()
    
    # Apply the selected transformation
    if transformation == 'raw':
        df_filtered.loc[:, 'transformed_time'] = df_filtered['time_since_case_start']
        x_title = "Time Since Case Start (Hours)"
        plot_title = "🕐 Event Time Distribution - Raw Time"
    else:  # log transformation
        df_filtered.loc[:, 'transformed_time'] = np.log1p(df_filtered['time_since_case_start'])
        x_title = "Log(Time Since Case Start + 1)"
        plot_title = "📊 Event Time Distribution - Log Time"
    
    # Calculate statistics for sorting
    if sorting == 'frequency':
        # Sort by frequency (most common first)
        event_order = df_filtered['concept:name'].value_counts().index.tolist()
    else:
        # Calculate statistics for each event type
        stats_df = df_filtered.groupby('concept:name')['transformed_time'].agg([
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
    
    # Create violin plot with custom ordering
    fig = px.violin(
        df_filtered, 
        x='transformed_time', 
        y='concept:name',
        orientation='h',
        box=True,
        title=plot_title,
        category_orders={'concept:name': event_order},
        color_discrete_sequence=['#3498db', '#e74c3c', '#2ecc71', '#f39c12']
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
