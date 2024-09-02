import requests
import json
from datetime import datetime, timedelta
import csv

# Define the endpoint
endpoint = "https://www.bitstamp.net/api/v2/ohlc/btcusd/"

# Set date range
end_date = datetime(2014, 5, 1)
start_date = datetime(2014, 1, 1)

# Calculate number of days
days_count = (end_date - start_date).days

# Define the parameters
params = {
    'step': 86400,  # 86400 seconds = 1 day
    'limit': days_count,
    'end': int(end_date.timestamp()),
}

# Prepare the request
req = requests.Request('GET', endpoint, params=params)
prepared = req.prepare()

# Print the full URL
print(f"Full request URL: {prepared.url}")

# Make the GET request
response = requests.Session().send(prepared)

# Save the data if request was successful
if response.status_code == 200:
    raw_data = response.json()
    
    # Save raw API response to JSON
    with open('bitstamp_ohlc_data_may_2014.json', 'w') as json_file:
        json.dump(raw_data, json_file, indent=4)
    
    # Prepare data for CSV
    daily_closes = []
    for candle in raw_data['data']['ohlc']:
        timestamp = int(candle['timestamp'])
        date = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d')
        close_price = candle['close']
        daily_closes.append({'Date': date, 'BTC_USD': close_price})

    # Sort by date (oldest first)
    daily_closes.sort(key=lambda x: x['Date'])

    # Save dates and close prices to CSV
    with open('bitstamp_btc_daily_closes_may_2014.csv', 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=['Date', 'BTC_USD'])
        writer.writeheader()
        writer.writerows(daily_closes)