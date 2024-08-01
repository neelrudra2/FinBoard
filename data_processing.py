import pandas as pd

def load_data(filepath):
    data = pd.read_csv(filepath)
    data.columns = data.columns.str.strip()  # Strip any extra spaces from column names
    
    print("Column names:", data.columns)  # Verify column names
    
    if 'date' not in data.columns:
        raise KeyError("The column 'date' does not exist in the CSV file.")
    
    data['date'] = pd.to_datetime(data['date'])
    data.set_index('date', inplace=True)
    data.dropna(inplace=True)
    return data

def add_moving_average(data, window=30):
    data['Moving_Avg'] = data['close'].rolling(window=window).mean()  # Updated to 'close'
    return data
