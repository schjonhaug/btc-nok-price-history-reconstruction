import os
import json
import pandas as pd


def bitstamp():
    # Set the data directory
    data_dir = os.path.join(os.path.dirname(__file__), 'data')

    # Read BTC/USD data from Bitstamp JSON file
    bitstamp_file = os.path.join(data_dir, 'bitstamp-btc-usd-may-2014.json')
    with open(bitstamp_file, 'r') as f:
        bitstamp_data = json.load(f)

    # Extract the 'ohlc' data
    ohlc_data = bitstamp_data['data']['ohlc']

    # Convert JSON data to DataFrame
    df = pd.DataFrame(ohlc_data)

    # Convert 'timestamp' to datetime and 'close' to float
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
    df['close'] = df['close'].astype(float)

    # Select only 'timestamp' and 'close' columns
    df = df[['timestamp', 'close']]

    # Convert DataFrame to list of lists (without labels)
    result = df.values.tolist()

    # Add 'Bitstamp' as the source for each data point
    result = [[date, price, 'Bitstamp'] for date, price in result]

    return result
