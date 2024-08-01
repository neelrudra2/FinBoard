import dash
from dash import dcc, html
from data_processing import load_data, add_moving_average
from visualizations import create_dash_figures

# Load and process data
data = load_data('data/all_stocks_5yr.csv')
data = add_moving_average(data)

# Create figures for Dash
stock_prices_fig, heatmap_fig = create_dash_figures(data)

# Create a Dash app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div([
    html.H1('Financial Data Dashboard'),
    dcc.Graph(
        id='stock-prices',
        figure=stock_prices_fig
    ),
    dcc.Graph(
        id='correlation-heatmap',
        figure=heatmap_fig
    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
