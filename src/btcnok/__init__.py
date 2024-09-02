from .mtgox import mtgox
from .bitstamp import bitstamp
from .btcnok import btcnok

def main() -> int:
    btc_usd_data = mtgox() + bitstamp()
    print("Combined Data:", btc_usd_data)
    btcnok(btc_usd_data)

    

    return 0
