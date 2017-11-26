from VanillaOption import *
from OptionData import *


def test_monte_carlo_model():
  ## Price American Binomial Option
  # Set up OptionData
  spot = 41.0
  rate = 0.08
  volatility = 0.30
  dividend = 0.0
  monte_carlo_data = OptionData(rate, spot, volatility, dividend)

  # Set up the option
  expiry = 1.0
  strike = 40.0
  monte_call = VanillaCallOption(strike, expiry)
  monte_put  = VanillaPutOption(strike,  expiry)
  
  # Set up Naive Monte Carlo
  replications = 100000
  time_steps = 1

  # Price the Call Option
  call_price = NaiveMonteCarloPricer(monte_call, monte_carlo_data, replications, time_steps)
  print("The call price from the Naive Monte Carlo Price Model is = {0:.4f}".format(call_price))

  # Price the Call Option
  put_price = NaiveMonteCarloPricer(monte_put, monte_carlo_data, replications, time_steps)
  print("The put price from the Naive Monte Carlo Price Model is = {0:.4f}".format(put_price))