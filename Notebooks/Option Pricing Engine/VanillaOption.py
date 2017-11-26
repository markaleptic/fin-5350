import numpy as np
from scipy.stats import binom


class VanillaOption(object):
  """An abstract interface for plain vanilla options."""

  def __init__(self, strike, expiry):
    self.strike = strike
    self.expiry = expiry

  def get_strike(self):
    return self.strike

  def get_expiry(self):
    return self.expiry

  def payoff(self, spot):
    pass


class VanillaCallOption(VanillaOption):
  """A concrete class for vanilla call options."""

  def payoff(self, spot):
    return np.maximum(spot - self.strike, 0.0)


class VanillaPutOption(VanillaOption):
  """A concrete class for vanilla put options."""

  def payoff(self, spot):
    return np.maximum(self.strike - spot, 0.0)


def EuropeanBinomialPricer(option, optiondata, steps):
  rate, spot, volatility, dividend = optiondata.get_data()
  expiry = option.get_expiry()
  H = expiry / steps
  numNodes = steps + 1

  up   = np.exp(((rate - dividend) * H) + volatility * np.sqrt(H))
  down = np.exp(((rate - dividend) * H) - volatility * np.sqrt(H))
  prob_up   = (np.exp((rate - dividend) * H) - down) / (up - down)
  prob_down = 1 - prob_up
    
  spot_t = 0.0
  payoff_t = 0.0
    
  for i in range(numNodes):
    spot_t = spot * (up ** (steps - i)) * (down ** i)
    payoff_t += option.payoff(spot_t) * binom.pmf(steps - i, steps, prob_up)
  price = payoff_t * np.exp(-rate * expiry)

  return price


def AmericanBinomialPricer(option, optiondata, steps):
  expiry = option.get_expiry()
  rate, spot, volatility, dividend = optiondata.get_data()
  nodes = steps + 1
  H = expiry / steps

  up = np.exp(((rate - dividend) * H) + volatility * np.sqrt(H))
  down = np.exp(((rate - dividend) * H) - volatility * np.sqrt(H))
  prob_up = (np.exp((rate - dividend) * H) - down) / (up - down)
  prob_down = 1 - prob_up
  disc = np.exp(-rate * H)
  dpu = disc * prob_up
  dpd = disc * prob_down

  call_t = np.zeros(nodes)
  spot_t = np.zeros(nodes)

  for i in range(nodes):
    spot_t[i] = spot * (up ** (steps - i)) * (down ** i)
    call_t[i] = option.payoff(spot_t[i])

  for i in range((steps - 1), -1, -1):
    for j in range(i+1):
      call_t[j] = dpu * call_t[j] + dpd * call_t[j+1]
      spot_t[j] = spot_t[j] / up
      call_t[j] = np.maximum(call_t[j], option.payoff(spot_t[j]))

  return call_t[0]


def NaiveMonteCarloPricer(option, optiondata, replications, time_steps):
  expiry = option.get_expiry()
  rate, spot, volatility, dividend = optiondata.get_data()
  H = expiry / time_steps

  z = np.random.normal(size = replications)
  spot_t = spot * np.exp((rate - dividend - 0.5 * volatility * volatility) * H + volatility * np.sqrt(H) * z)
  payoff_t = option.payoff(spot_t)

  price = payoff_t.mean() * np.exp(-rate * H)

  return price
