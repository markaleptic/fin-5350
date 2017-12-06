from OptionData import *
from VanillaOption import *

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

def main():
  # Test European Binomial Pricing Model
  print("Pricing a Vanilla European Option with the Binomial Pricing Model")
  test_european_model()

  # Test American Binomial Pricing Model
  print("\n\nPricing a Vanilla American Option with the Binomial Pricing Model")
  test_american_model()

  # Test Naive Monte Carlo Pricing Model
  print("\n\nPricing a Vanilla Option with the Naive Monte Carlo Pricing Model")
  test_monte_carlo_model()


main()
