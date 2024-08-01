import plotly.express as px

def create_dash_figures(data):
    # Plot stock prices
    stock_prices_fig = {
        'data': [
            {'x': data.index, 'y': data['close'], 'type': 'line', 'name': 'Close Price'},  # Updated to 'close'
            {'x': data.index, 'y': data['Moving_Avg'], 'type': 'line', 'name': '30-Day Moving Avg'},
        ],
        'layout': {
            'title': 'Stock Prices',
            'xaxis': {'title': 'Date'},
            'yaxis': {'title': 'Price'}
        }
    }

    # Filter numeric columns only for correlation
    numeric_data = data.select_dtypes(include=['number'])
    heatmap_fig = px.imshow(numeric_data.corr(), text_auto=True, color_continuous_scale='viridis')  # Changed to 'viridis'
    heatmap_fig.update_layout(title='Correlation Heatmap')

    return stock_prices_fig, heatmap_fig
