# Bitcoin Norwegian Krone (BTC/NOK) Price History Reconstruction

This repository contains the code and data used to reconstruct the Bitcoin Norwegian Krone (BTC/NOK) price history from 2010 to 2014, prior to [Bitmynt](https://bitmynt.no) having their own ticker. At that time, Bitmynt was the sole Norwegian Bitcoin exchange. Initially, they used the [MtGox](https://en.wikipedia.org/wiki/Mt._Gox) rate in USD, converted to NOK using the latest exchange rate from [Norges Bank](https://www.norges-bank.no/en/), with an additional 2.5% margin.

During this period, Norges Bank published the daily exchange rate around 14:30 CET. Consequently, Friday's krone exchange rate was valid until 14:30 on Monday. However, due to data limitations, we use the Friday rate for Saturday and Sunday, and the Monday rate for Monday.

From January 2014 onward, Bitmynt began adjusting the margin in response to the increasing divergence of the MtGox rate from other exchanges. Therefore, for practical purposes, we have switched to using [Bitstamp](https://www.bitstamp.net) data from the beginning of 2014 until the start of the Bitmynt ticker history.


## Data Sources

These are the data sources used to reconstruct the price history:

* [MtGox](https://raw.githubusercontent.com/marcosebarreto/Datasets/master/BCHARTS-MTGOXUSD.csv) BTC/USD exchange rates from 2010-2014  
* [Bitstamp](https://www.bitstamp.net/api/v2/ohlc/btcusd/?step=86400&limit=120&end=1398895200) BTC/USD exchange rates from 2014
* [Norges Bank](https://data.norges-bank.no/api/data/EXR/B.USD.NOK.SP?format=csv&startPeriod=2010-07-16&endPeriod=2014-06-01&bom=include) USD/NOK exchange rates from 2010-2014


 They are saved in the `src/btc_nok_reconstruction/data` folder and are the basis for the reconstructions.





## Usage



```sh
rye sync
rye run btc_nok_reconstruction
```

This will create a CSV file in the root folder called [btc-nok-price-history-reconstruction.csv](btc-nok-price-history-reconstruction.csv) with the reconstructed BTC/NOK price history.
