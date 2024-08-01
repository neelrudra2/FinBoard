<h1>Financial Data Analysis Dashboard</h1>

<h2>Overview</h2>
The Financial Data Analysis Dashboard is a web application designed to visualize and analyze financial data. It displays key metrics such as stock prices, trading volumes, and market indices, providing users with insightful visualizations to track and understand market trends.

<h2>Features</h2>
1. Stock Price Visualization: Displays stock prices over time using line charts.<br>
2. Trading Volume Analysis: Visualizes trading volumes to understand market activity.</br>
3. Correlation Heatmap: Provides a heatmap of the correlation between different financial metrics.</br>
4. Interactive Interface: Users can interact with the visualizations, zoom in/out, and hover over data points for detailed information.

<h2>Importance and Use Cases</h2>
* Market Analysis: Helps investors and analysts track stock performance and market trends.</br>
* Decision Making: Provides critical insights that aid in making informed investment decisions.</br>
* Educational Tool: Useful for students and educators in finance to understand data visualization and financial analysis.

<h2>How it works</h2>
<h3>1.  Data Loading:</h3>
The project includes a 'data_processing.py' script that handles loading and preprocessing the financial data from a CSV file.
```py
import pandas as pd

def load_data(filepath):
    data = pd.read_csv(filepath)
    data['date'] = pd.to_datetime(data['date'])  # Convert date column to datetime
    return data
```

<h3>2. Data Visualization:</h3>
The visualization script contains functions to create visualizations using Plotly Express. A line chart displays stock prices over time.
```py
import plotly.express as px

def create_dash_figures(data):
    stock_prices_fig = px.line(data, x='date', y='close', title='Stock Prices Over Time')
    numeric_data = data.select_dtypes(include=['float64', 'int64'])  # Select numeric columns
    heatmap_fig = px.imshow(numeric_data.corr(), text_auto=True, color_continuous_scale='RdBu_r', title='Correlation Heatmap')
    return stock_prices_fig, heatmap_fig
```

<h3>3. Web Application:</h3>
The main application is built using Dash, which integrates the visualizations into a web interface. The application runs on a local server.

<h2>Technologies Used:</h2>
1. Python: For data processing and backend logic.
2. Pandas: For data manipulation and analysis.
3. Plotly: For creating interactive visualizations.
4. Dash: For building the web application and integrating the visualizations.
5. HTML/CSS: For structuring and styling the web interface.


<h2>Project Screenshot:</h2>
