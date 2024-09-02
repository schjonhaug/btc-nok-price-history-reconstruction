import csv
from datetime import datetime

btc_nok_prices = {}

with open('btc_nok_historical.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        date_str, _, _, _, btc_nok_with_fee = row
        date = datetime.strptime(date_str, '%Y-%m-%d')
        if date.day == 1:
            btc_nok_prices[date_str] = float(btc_nok_with_fee)

print(btc_nok_prices)