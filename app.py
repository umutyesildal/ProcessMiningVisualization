import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html, Input, Output
import logging
import numpy as np

logging.basicConfig(level=logging.INFO)

# Load preprocessed data
df = pd.read_csv('processed_bpi2017.csv')
logging.info(f"Loaded processed_bpi2017.csv with shape: {df.shape}")

# Apply log transformation
df['log_time'] = np.log1p(df['time_since_case_start'])
logging.info(f"Log transformation applied. log_time min: {df['log_time'].min()}, max: {df['log_time'].max()}")

# Initial app setup
app = dash.Dash(__name__)
app.title = "Event Type Distribution Visualization"

# Statistical sorting options
sorting_options = ['min', 'max', 'mean', 'median', 'Q1', 'Q3']

# Compute stats for sorting
def compute_stats(df):
    logging.info("Computing stats for sorting...")
    stats = df.groupby('concept:name')['time_since_case_start'].agg(['min', 'max', 'mean', 'median'])
    stats['Q1'] = df.groupby('concept:name')['time_since_case_start'].quantile(0.25)
    stats['Q3'] = df.groupby('concept:name')['time_since_case_start'].quantile(0.75)
    stats.reset_index(inplace=True)
    logging.info(f"Stats computed. Shape: {stats.shape}")
    return stats

stats = compute_stats(df)

# App layout
app.layout = html.Div([
    dcc.Loading(
        id="loading-violin",
        type="circle",
        fullscreen=True,
        children=[
            html.H1("Interactive Event Type Distribution Over Time", style={'textAlign': 'center'}),
            html.Div([
                html.Label("Sort Event Types by:"),
                dcc.Dropdown(
                    id='sort-dropdown',
                    options=[{'label': opt.capitalize(), 'value': opt} for opt in sorting_options],
                    value='median',
                    clearable=False,
                    style={'width': '200px', 'margin-bottom': '20px'}
                )
            ], style={'textAlign': 'center'}),
            dcc.Graph(id='violin-plot', style={'height': '90vh', 'width': '100vw'})
        ]
    )
])

# Callback for interactivity
@app.callback(
    Output('violin-plot', 'figure'),
    [Input('sort-dropdown', 'value')]
)
def update_violin(sort_by):
    logging.info(f"update_violin called with sort_by={sort_by}")
    # Find the most frequent event type
    most_frequent = df['concept:name'].value_counts().idxmax()
    df_single = df[df['concept:name'] == most_frequent]
    logging.info(f"Plotting {len(df_single)} rows for event type: {most_frequent}")
    try:
        fig = px.violin(
            df_single,
            y='concept:name',
            x='log_time',
            orientation='h',
            box=True,
            points='all',
            width=800,
            height=400,
            color=None
        )
        fig.update_traces(meanline_visible=True, spanmode='hard', scalemode='width', side='both', jitter=0.3, pointpos=0)
        fig.update_layout(
            xaxis_title="Log(Time Since Case Start + 1) [Hours]",
            yaxis_title="Event Type",
            margin=dict(l=100, r=50, t=50, b=50),
            autosize=True,
            height=400,
            width=800,
            plot_bgcolor='white',
            paper_bgcolor='white',
            title=f"Violin Plot for Event Type: {most_frequent} (Log Time)"
        )
        logging.info("Single event type violin plot (log time) created successfully.")
        return fig
    except Exception as e:
        logging.error(f"Error in update_violin: {e}")
        raise

if __name__ == '__main__':
    app.run(debug=True)
