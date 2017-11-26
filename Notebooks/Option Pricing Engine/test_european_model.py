from VanillaOption import *
from OptionData import *


def test_european_model():
  ## Price European Binomial Option
  # Set up OptionData
  spot = 41.0
  rate = 0.08
  volatility = 0.30
  dividend = 0.0
  EuroData = OptionData(rate, spot, volatility, dividend)

  # Set up the option
  expiry = 1.0
  strike = 40.0
  Euro_Call = VanillaCallOption(strike, expiry)
  Euro_Put  = VanillaPutOption(strike, expiry)
  steps = 3

  # Price the Call Option
  call_price = EuropeanBinomialPricer(Euro_Call, EuroData, steps)
  print("The call price from the European Binomial Price Model is = {0:.4f}".format(call_price))

  # Price the Put Option
  put_price = EuropeanBinomialPricer(Euro_Put, EuroData, steps)
  print("The put price from the European Binomial Price Model is = {0:.4f}".format(put_price))
