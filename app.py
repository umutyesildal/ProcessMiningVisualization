import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html, Input, Output
import logging
import numpy as np

logging.basicConfig(level=logging.INFO)

# Load processed Road Traffic Fines event log
df = pd.read_csv('processed_trafficfines.csv')
logging.info(f"Loaded processed_trafficfines.csv with shape: {df.shape}")

# Log transformation for time since case start (optional, can comment out)
df['log_time'] = np.log1p(df['time_since_case_start'])
logging.info(f"Log transformation applied. log_time min: {df['log_time'].min()}, max: {df['log_time'].max()}")

# --- Load quantile-clipped and inter-event time processed data ---
df_quantile = pd.read_csv('trafficfines_filtered_quantile.csv')
df_interevent = pd.read_csv('trafficfines_interevent_quantile.csv')

app = dash.Dash(__name__)
app.title = "Traffic Fines Event Type Distribution Visualization"

sorting_options = ['min', 'max', 'mean', 'median', 'Q1', 'Q3']

def compute_stats(df, x_col):
    logging.info("Computing stats for sorting...")
    stats = df.groupby('concept:name')[x_col].agg(['min', 'max', 'mean', 'median'])
    stats['Q1'] = df.groupby('concept:name')[x_col].quantile(0.25)
    stats['Q3'] = df.groupby('concept:name')[x_col].quantile(0.75)
    stats.reset_index(inplace=True)
    logging.info(f"Stats computed. Shape: {stats.shape}")
    return stats

stats = compute_stats(df, 'time_since_case_start')

app.layout = html.Div([
    dcc.Loading(
        id="loading-violin",
        type="circle",
        fullscreen=True,
        children=[
            html.H1("Traffic Fines Event Type Distribution Over Time", style={'textAlign': 'center'}),
            html.Div([
                html.Label("Data Type:"),
                dcc.Dropdown(
                    id='data-type-dropdown',
                    options=[
                        {'label': 'Time Since Case Start', 'value': 'quantile'},
                        {'label': 'Inter-Event Time', 'value': 'interevent'}
                    ],
                    value='quantile',
                    clearable=False,
                    style={'width': '250px', 'margin-bottom': '20px', 'display': 'inline-block'}
                ),
                html.Label("Sort Event Types by:", style={'margin-left': '40px'}),
                dcc.Dropdown(
                    id='sort-dropdown',
                    options=[{'label': opt.capitalize(), 'value': opt} for opt in sorting_options],
                    value='median',
                    clearable=False,
                    style={'width': '200px', 'margin-bottom': '20px', 'display': 'inline-block'}
                )
            ], style={'textAlign': 'center'}),
            dcc.Graph(id='violin-plot', style={'height': '90vh', 'width': '100vw'})
        ]
    )
])

@app.callback(
    Output('violin-plot', 'figure'),
    [Input('sort-dropdown', 'value'), Input('data-type-dropdown', 'value')]
)
def update_violin(sort_by, data_type):
    logging.info(f"update_violin called with sort_by={sort_by}, data_type={data_type}")
    if data_type == 'quantile':
        df_plot = df_quantile
        x_col = 'log_time'
        x_title = "Log(Time Since Case Start + 1) [Seconds]"
    else:
        df_plot = df_interevent
        x_col = 'log_inter_event_time'
        x_title = "Log(Inter-Event Time + 1) [Seconds]"
    # Compute stats for sorting
    stats = df_plot.groupby('concept:name')[x_col.replace('log_', '')].agg(['min', 'max', 'mean', 'median'])
    stats['Q1'] = df_plot.groupby('concept:name')[x_col.replace('log_', '')].quantile(0.25)
    stats['Q3'] = df_plot.groupby('concept:name')[x_col.replace('log_', '')].quantile(0.75)
    stats.reset_index(inplace=True)
    sorted_events = stats.sort_values(by=sort_by)['concept:name']
    df_small = df_plot[df_plot['concept:name'].isin(sorted_events)]
    try:
        fig = px.violin(
            df_small,
            y='concept:name',
            x=x_col,
            category_orders={'concept:name': list(sorted_events)},
            orientation='h',
            box=True,
            points='all',
            width=1200,
            height=800,
            color=None
        )
        fig.update_traces(meanline_visible=True, spanmode='hard', scalemode='width', side='both', jitter=0.3, pointpos=0)
        fig.update_layout(
            xaxis_title=x_title,
            yaxis_title="Event Type",
            margin=dict(l=200, r=50, t=50, b=50),
            autosize=True,
            height=800,
            width=1200,
            plot_bgcolor='white',
            paper_bgcolor='white',
        )
        logging.info("Violin plot created successfully.")
        return fig
    except Exception as e:
        logging.error(f"Error in update_violin: {e}")
        raise

if __name__ == '__main__':
    app.run(debug=True)
