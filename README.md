# Bitcoin Norwegian Krone (BTC/NOK) Price History Reconstruction

This repository contains the code and data used to reconstruct the Bitcoin Norwegian Krone (BTC/NOK) price history between 2010 and 2014, before Bitmynt had their own ticker. Back then, Bitmynt was the only Norwegian Bitcoin exchange and in the beginning they used the MtGox rate in USD converted to NOK with the latest exchange rate from Norges Bank, and then with a 2.5% margin.

During that period, Norges Bank published the daily rate at around 14:30, so Friday's krone exchange rate was valid until 14:30 on Monday. This however, is not possible to reconstruct with the data available to us, so we use the Friday rate for Saturday and Sunday, and then the Monday rate for Monday.

Bitmynt also had a transition period from January 2014 onward, where they continuously adjusted the margin in line with the MtGox rate becoming increasingly more divergent from other exchanges. So, for practical purposes, we have switched to Bitstamp from the beginning of 2014 until the Bitmynt ticker history starts.


## Data Sources

These are the data sources used to reconstruct the price history:

### MtGox

https://raw.githubusercontent.com/marcosebarreto/Datasets/master/BCHARTS-MTGOXUSD.csv

### Bitstamp

* https://www.bitstamp.net/api/v2/ohlc/btcusd/?step=86400&limit=120&end=1398895200

### Norges Bank

https://data.norges-bank.no/api/data/EXR/B.USD.NOK.SP?format=csv&startPeriod=2010-07-16&endPeriod=2014-02-25&bom=include
 




They are saved in the `sources` folder and are the basis for the reconstructions.


## Setup
```sh
pip install -r requirements.txt
```

## Usage
