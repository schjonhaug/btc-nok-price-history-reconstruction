import pandas as pd
import requests
from io import StringIO
import os

# Fetch BTC/USD data
btc_usd_url = "https://raw.githubusercontent.com/marcosebarreto/Datasets/master/BCHARTS-MTGOXUSD.csv"
btc_usd_data = pd.read_csv(btc_usd_url)
btc_usd_data['Date'] = pd.to_datetime(btc_usd_data['Date'])
btc_usd_data.set_index('Date', inplace=True)

# Fetch USD/NOK data
usd_nok_url = "https://data.norges-bank.no/api/data/EXR/B.USD.NOK.SP?format=csv&startPeriod=2010-07-16&endPeriod=2014-02-25&bom=include"
response = requests.get(usd_nok_url)
usd_nok_data = pd.read_csv(StringIO(response.text), sep=';', decimal=',', thousands=' ', parse_dates=['TIME_PERIOD'])
usd_nok_data = usd_nok_data.rename(columns={'TIME_PERIOD': 'Date', 'OBS_VALUE': 'USD_NOK'})
usd_nok_data.set_index('Date', inplace=True)

# Create a date range that includes July 16, 2010
all_dates = pd.date_range(start=min(btc_usd_data.index.min(), usd_nok_data.index.min()), end=btc_usd_data.index.max())

# Reindex USD/NOK data and forward fill
usd_nok_data = usd_nok_data.reindex(all_dates).ffill()

# Combine datasets
combined_data = pd.concat([btc_usd_data, usd_nok_data], axis=1)

# Calculate BTC/NOK price and round to 6 decimal places
combined_data['BTC_NOK'] = (combined_data['Close'].astype(float) * combined_data['USD_NOK'].astype(float)).round(6)

# Add 2.5% to the NOK price and round to 6 decimal places
combined_data['BTC_NOK_with_fee'] = (combined_data['BTC_NOK'] * 1.025).round(6)

# Reset index to make Date a column again
combined_data.reset_index(inplace=True)

# Rename 'Close' to 'BTC_USD' for clarity
combined_data = combined_data.rename(columns={'Close': 'BTC_USD', 'index': 'Date'})

# Select only the desired columns
final_data = combined_data[['Date', 'BTC_USD', 'USD_NOK', 'BTC_NOK', 'BTC_NOK_with_fee']]

# Remove rows where BTC_USD is NaN (this will remove July 16, 2010)
final_data = final_data.dropna(subset=['BTC_USD'])

# Create final CSV
try:
    csv_path = 'btc_nok_historical.csv'
    final_data.to_csv(csv_path, index=False)
    print(f"CSV file '{csv_path}' has been created with {len(final_data)} rows.")
    print(f"File path: {os.path.abspath(csv_path)}")
except Exception as e:
    print(f"Error creating CSV: {e}")

print("\nFinal data (first few rows):")
print(final_data.head())

print("\nNumber of rows in final dataset:")
print(f"Final data: {len(final_data)}")