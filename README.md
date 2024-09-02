# Bitcoin Norwegian Krone (BTC/NOK) Price History Reconstruction

This repository contains the code and data used to reconstruct the Bitcoin Norwegian Krone (BTC/NOK) price history from 2010 to 2014, used by Norway’s oldest Bitcoin OTC, [Bitmynt](https://bitmynt.no), before they had their own ticker. Initially, they used the [MtGox](https://en.wikipedia.org/wiki/Mt._Gox) rate in USD, converted to NOK using the latest exchange rate from [Norges Bank](https://www.norges-bank.no/en/), with an additional 2.5% margin.

During this period, Norges Bank published the daily exchange rate around 14:30 CET. Consequently, Friday's krone exchange rate was valid until 14:30 on Monday. However, due to data limitations, we use the Friday rate for Saturday and Sunday, and the Monday rate for Monday.

From January 2014 onward, Bitmynt began adjusting the margin in response to the increasing divergence of the MtGox rate from other exchanges. Therefore, for practical purposes, we have switched to using [Bitstamp](https://www.bitstamp.net) data from the beginning of 2014 until the start of the Bitmynt ticker history.


## Input

These are the data sources used to reconstruct the price history:

* [MtGox](https://raw.githubusercontent.com/marcosebarreto/Datasets/master/BCHARTS-MTGOXUSD.csv) BTC/USD exchange rates from 2010-2014  
* [Bitstamp](https://www.bitstamp.net/api/v2/ohlc/btcusd/?step=86400&limit=120&end=1398895200) BTC/USD exchange rates from 2014
* [Norges Bank](https://data.norges-bank.no/api/data/EXR/B.USD.NOK.SP?format=csv&startPeriod=2010-07-16&endPeriod=2014-06-01&bom=include) USD/NOK exchange rates from 2010-2014

They are saved in the `src/btc_nok_reconstruction/data` folder and are the basis for the reconstructions.

One minor issue is that MtGox prices are missing for the period 2011-06-20 to 2011-06-25.

```csv
2011-06-27,16.45001,18.0,15.0,16.75004,31452.5444794,535096.370101,17.0128165768
2011-06-26,17.51001,17.51001,14.01,16.45001,15053.9269271,234621.797323,15.585421562
2011-06-25,0.0,0.0,0.0,0.0,0.0,0.0,0.0
2011-06-24,0.0,0.0,0.0,0.0,0.0,0.0,0.0
2011-06-23,0.0,0.0,0.0,0.0,0.0,0.0,0.0
2011-06-22,0.0,0.0,0.0,0.0,0.0,0.0,0.0
2011-06-21,0.0,0.0,0.0,0.0,0.0,0.0,0.0
2011-06-20,0.0,0.0,0.0,0.0,0.0,0.0,0.0
2011-06-19,16.85,18.8766,16.85,17.51,30176.739,536267.379238,17.7708856891
2011-06-18,15.9635,16.9499,15.052,16.89,35536.552,569949.344478,16.0383974359
```

To resolve this discrepancy, we interpolate the missing values.

## Output

Running the `btc_nok_reconstruction.py` script will create a CSV file in the root folder called [btc-nok-price-history-reconstruction.csv](btc-nok-price-history-reconstruction.csv) with the reconstructed BTC/NOK price history.

For convenience, the file is also included in the repository.
