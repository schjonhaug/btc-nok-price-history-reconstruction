from .mtgox import mtgox
from .bitstamp import bitstamp
from .btcnok import btcnok
from .interpolation import interpolate_zero_values

def main() -> int:

 

     
    mtgox_data = interpolate_zero_values(mtgox())
 
    bitstamp_data = bitstamp()
 

    btcnok(mtgox_data + bitstamp_data)

    

    return 0
