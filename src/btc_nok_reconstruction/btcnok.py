import pandas as pd
from io import StringIO
import os

def btcnok(btc_usd_data):
    """
    Convert BTC/USD data to BTC/NOK using historical USD/NOK exchange rates.

    Parameters:
    btc_usd_data (list of lists): Historical BTC/USD data with each sublist containing ['Date', 'Close'].

    Returns:
    None: Outputs a CSV file with the reconstructed BTC/NOK prices.
    """
    # Convert the input list of lists to a DataFrame
    btc_usd_df = pd.DataFrame(btc_usd_data, columns=['Date', 'Close', 'Source'])
    btc_usd_df['Date'] = pd.to_datetime(btc_usd_df['Date'])
    btc_usd_df.set_index('Date', inplace=True)

    # Read USD/NOK data from local file
    usd_nok_file = os.path.join('src/btc_nok_reconstruction/data', 'norges-bank-usd-nok-from-2010-07-16-to-2014-06-01.csv')
    usd_nok_data = pd.read_csv(usd_nok_file, sep=';', decimal=',', thousands=' ', parse_dates=['TIME_PERIOD'])
    usd_nok_data = usd_nok_data.rename(columns={'TIME_PERIOD': 'Date', 'OBS_VALUE': 'USD_NOK'})
    usd_nok_data.set_index('Date', inplace=True)

    # Create a date range that includes July 16, 2010. We need to include this date, 
    # because the first BTC/USD is from July 17, 2010, which was a Saturday. 
    # And Norges Bank do not publish the exchange rate on Saturdays.
    all_dates = pd.date_range(start=min(btc_usd_df.index.min(), usd_nok_data.index.min()), end=btc_usd_df.index.max())

    # Reindex USD/NOK data and forward fill missing values
    usd_nok_data = usd_nok_data.reindex(all_dates).ffill()

    # Combine datasets
    combined_data = pd.concat([btc_usd_df, usd_nok_data], axis=1)

    # Calculate BTC/NOK price with 2.5% fee and round to 2 decimal places
    combined_data['BTC_NOK'] = (combined_data['Close'].astype(float) * combined_data['USD_NOK'].astype(float) * 1.025).round(2)

    # Reset index to make Date a column again
    combined_data.reset_index(inplace=True)

    # Rename 'Close' to 'BTC_USD' for clarity and capitalize all column names
    combined_data = combined_data.rename(columns={
        'Close': 'BTC_USD',
        'index': 'DATE',
        'USD_NOK': 'USD_NOK',
        'BTC_NOK': 'BTC_NOK',
        'Source': 'SOURCE'
    })

    # Select only the desired columns, including the Source column
    final_data = combined_data[['DATE', 'BTC_USD', 'USD_NOK', 'BTC_NOK', 'SOURCE']]

    # Remove rows where BTC_USD is NaN
    final_data = final_data.dropna(subset=['BTC_USD'])

    # Create final CSV
    try:
        csv_path = 'btc-nok-price-history-reconstruction.csv'
        final_data.to_csv(csv_path, index=False, columns=['DATE', 'BTC_USD', 'USD_NOK', 'BTC_NOK', 'SOURCE'])
        print(f"CSV file '{csv_path}' has been created with {len(final_data)} rows.")
        print(f"File path: {os.path.abspath(csv_path)}")
    except Exception as e:
        print(f"Error creating CSV: {e}")

    print("\nFinal data (first few rows):")
    print(final_data.head())

    print("\nNumber of rows in final dataset:")
    print(f"Final data: {len(final_data)}")
