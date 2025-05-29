import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html, Input, Output
import logging
import numpy as np
import dash_bootstrap_components as dbc

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

# Sidebar layout
sidebar = html.Div([
    html.H2("Filters", className="display-6"),
    html.Hr(),
    html.Label("Event Type:"),
    dcc.Dropdown(
        id='event-type-dropdown',
        options=[{'label': e, 'value': e} for e in sorted(df_quantile['concept:name'].unique())],
        value=None,
        multi=True,
        placeholder="All event types"
    ),
    html.Br(),
    html.Label("Outcome (if available):"),
    dcc.Dropdown(
        id='outcome-dropdown',
        options=[{'label': o, 'value': o} for o in sorted(df_quantile['lifecycle:transition'].unique())] if 'lifecycle:transition' in df_quantile.columns else [],
        value=None,
        multi=True,
        placeholder="All outcomes"
    ),
    html.Br(),
    html.Label("Sort Event Types by:"),
    dcc.Dropdown(
        id='sort-dropdown',
        options=[{'label': opt.capitalize(), 'value': opt} for opt in sorting_options],
        value='median',
        clearable=False
    ),
], style={
    'position': 'fixed',
    'top': 0,
    'left': 0,
    'bottom': 0,
    'width': '300px',
    'padding': '30px 10px',
    'background-color': '#f8f9fa',
    'overflowY': 'auto',
    'zIndex': 1000
})

# Main content with tabs
content = html.Div([
    dcc.Tabs(id='tabs', value='tab-quantile', children=[
        dcc.Tab(label='Time Since Case Start', value='tab-quantile'),
        dcc.Tab(label='Inter-Event Time', value='tab-interevent'),
        # Add more tabs for other analyses
    ]),
    html.Div(id='tab-content', style={'margin-left': '320px', 'padding': '20px'})
])

app.layout = html.Div([
    sidebar,
    content
])

@app.callback(
    Output('tab-content', 'children'),
    [Input('tabs', 'value'),
     Input('sort-dropdown', 'value'),
     Input('event-type-dropdown', 'value'),
     Input('outcome-dropdown', 'value')]
)
def render_tab(tab, sort_by, event_types, outcomes):
    if tab == 'tab-quantile':
        df_plot = df_quantile.copy()
        x_col = 'log_time'
        x_title = "Log(Time Since Case Start + 1) [Seconds]"
    elif tab == 'tab-interevent':
        df_plot = df_interevent.copy()
        x_col = 'log_inter_event_time'
        x_title = "Log(Inter-Event Time + 1) [Seconds]"
    else:
        return html.Div("Tab not implemented.")
    # Filter by event type
    if event_types:
        df_plot = df_plot[df_plot['concept:name'].isin(event_types)]
    # Filter by outcome if available
    if outcomes and 'lifecycle:transition' in df_plot.columns:
        df_plot = df_plot[df_plot['lifecycle:transition'].isin(outcomes)]
    # Map log column to raw column name
    x_raw_col_map = {
        'log_time': 'time_since_case_start',
        'log_inter_event_time': 'inter_event_time'
    }
    raw_col = x_raw_col_map.get(x_col, x_col)
    # Compute stats for sorting
    stats = df_plot.groupby('concept:name')[raw_col].agg(['min', 'max', 'mean', 'median'])
    stats['Q1'] = df_plot.groupby('concept:name')[raw_col].quantile(0.25)
    stats['Q3'] = df_plot.groupby('concept:name')[raw_col].quantile(0.75)
    stats.reset_index(inplace=True)
    sorted_events = stats.sort_values(by=sort_by)['concept:name']
    df_small = df_plot[df_plot['concept:name'].isin(sorted_events)]
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
    return dcc.Graph(figure=fig, style={'height': '90vh', 'width': '100vw'})

if __name__ == '__main__':
    app.run(debug=True)
