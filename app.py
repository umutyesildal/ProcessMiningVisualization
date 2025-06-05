import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html, Input, Output
import numpy as np

# Load processed traffic fines data
df = pd.read_csv('data/processed_trafficfines.csv')

# Get top 4 event types
top_events = df['concept:name'].value_counts().head(4).index.tolist()
df_filtered = df[df['concept:name'].isin(top_events)]

# Create Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Traffic Fines Process Mining Visualization", style={'textAlign': 'center', 'marginBottom': '30px'}),
    
    # Control panel with dropdowns
    html.Div([
        # Time transformation dropdown
        html.Div([
            html.Label("Select Time Transformation:", style={'fontWeight': 'bold', 'marginBottom': '10px'}),
            dcc.Dropdown(
                id='time-transformation-dropdown',
                options=[
                    {'label': 'Raw Time (Hours)', 'value': 'raw'},
                    {'label': 'Log Time (Log(Hours + 1))', 'value': 'log'},
                    {'label': 'Square Root Time (sqrt(Hours))', 'value': 'sqrt'}
                ],
                value='log',  # Default to log transformation
                style={'width': '350px'}
            )
        ], style={'display': 'inline-block', 'marginRight': '40px', 'verticalAlign': 'top'}),
        
        # Sorting dropdown
        html.Div([
            html.Label("Sort Event Types By:", style={'fontWeight': 'bold', 'marginBottom': '10px'}),
            dcc.Dropdown(
                id='sorting-dropdown',
                options=[
                    {'label': 'Frequency (Most Common First)', 'value': 'frequency'},
                    {'label': 'Mean Time', 'value': 'mean'},
                    {'label': 'Median Time', 'value': 'median'},
                    {'label': 'Minimum Time', 'value': 'min'},
                    {'label': 'Maximum Time', 'value': 'max'},
                    {'label': '25th Percentile (Q1)', 'value': 'q1'},
                    {'label': '75th Percentile (Q3)', 'value': 'q3'}
                ],
                value='frequency',  # Default to frequency sorting
                style={'width': '350px'}
            )
        ], style={'display': 'inline-block', 'verticalAlign': 'top'})
        
    ], style={'margin': '20px auto', 'textAlign': 'center'}),
    
    # Graph placeholder
    dcc.Graph(id='violin-plot')
], style={'padding': '20px'})

# Callback to update the violin plot based on selected transformation and sorting
@app.callback(
    Output('violin-plot', 'figure'),
    [Input('time-transformation-dropdown', 'value'),
     Input('sorting-dropdown', 'value')]
)
def update_violin_plot(transformation, sorting):
    # Apply the selected transformation
    if transformation == 'raw':
        df_filtered['transformed_time'] = df_filtered['time_since_case_start']
        x_title = "Time Since Case Start (Hours)"
        plot_title = "Traffic Fines: Event Time Distribution (Raw Time)"
    elif transformation == 'log':
        df_filtered['transformed_time'] = np.log1p(df_filtered['time_since_case_start'])
        x_title = "Log(Time Since Case Start + 1)"
        plot_title = "Traffic Fines: Event Time Distribution (Log Time)"
    elif transformation == 'sqrt':
        df_filtered['transformed_time'] = np.sqrt(df_filtered['time_since_case_start'])
        x_title = "sqrt(Time Since Case Start) (sqrt(Hours))"
        plot_title = "Traffic Fines: Event Time Distribution (Square Root Time)"
    
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
        category_orders={'concept:name': event_order}
    )
    
    fig.update_layout(
        xaxis_title=x_title,
        yaxis_title="Event Type",
        height=500,
        width=1000,
        margin={'t': 80, 'l': 250, 'r': 50, 'b': 80}
    )
    
    return fig

if __name__ == '__main__':
    app.run(debug=True)
