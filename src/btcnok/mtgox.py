import pandas as pd
import os

def mtgox():
   

    # Set the data directory
    data_dir = 'src/btcnok/data'

    # Read BTC/USD data from MtGox
    btc_usd_file = os.path.join(data_dir, 'mtgox-btc-usd-from-2010-07-17-to-2014-02-25.csv')
    btc_usd_data = pd.read_csv(btc_usd_file)
    
    # Convert 'Date' to datetime and 'Close' to float
    btc_usd_data['Date'] = pd.to_datetime(btc_usd_data['Date'])
    btc_usd_data['Close'] = btc_usd_data['Close'].astype(float)
    
    # Filter out data from 2014
    btc_usd_data = btc_usd_data[btc_usd_data['Date'].dt.year < 2014]
    
    # Select only 'Date' and 'Close' columns
    btc_usd_data = btc_usd_data[['Date', 'Close']]
    
    # Sort data by 'Date' in ascending order (oldest first)
    btc_usd_data = btc_usd_data.sort_values(by='Date', ascending=True)
    
    # Convert DataFrame to list of lists (without labels)
    result = btc_usd_data.values.tolist()
    
    return result




   