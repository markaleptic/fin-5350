from VanillaOption import *
from OptionData import *
from test_european_model import *
from test_american_model import *
from test_monte_carlo_model import *


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
