from VanillaOption import *
from OptionData import *


def test_american_model():
  ## Price American Binomial Option
  # Set up OptionData
  spot = 41.0
  rate = 0.08
  volatility = 0.30
  dividend = 0.0
  AmericanData = OptionData(rate, spot, volatility, dividend)

  # Set up the option
  expiry = 1.0
  strike = 40.0
  yankee_call = VanillaCallOption(strike, expiry)
  yankee_put  = VanillaPutOption(strike,  expiry)
  steps = 3

  # Price the Call Option
  call_price = AmericanBinomialPricer(yankee_call, AmericanData, steps)
  print("The call price from the American Binomial Price Model is = {0:.4f}".format(call_price))

  # Price the Call Option
  put_price = AmericanBinomialPricer(yankee_put, AmericanData, steps)
  print("The put price from the American Binomial Price Model is = {0:.4f}".format(put_price))