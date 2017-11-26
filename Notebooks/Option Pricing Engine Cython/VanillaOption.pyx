cdef class VanillaOption:
  """An abstract interface for plain vanilla options."""

  def __init__(self, strike, expiry):
    self._strike = strike
    self._expiry = expiry

  property expiry:
    def __get__(self):
      return self._expiry
    def __set__(self, expiry):
      self._expiry = expiry

  property strike:
    def __get__(self):
      return self._strike

    def __set__(self, strike):
      self._strike = strike

  cpdef payoff(self, spot):
    pass


cdef class VanillaCallOption(VanillaOption):
  """A concrete class for vanilla call options."""

  cpdef payoff(self, double spot):
    return np.maximum(spot - self.strike, 0.0)


cdef class VanillaPutOption(VanillaOption):
  """A concrete class for vanilla put options."""

  cpdef payoff(self, double spot):
    return np.maximum(self.strike - spot, 0.0)


cdef double EuropeanBinomialPricer(VanillaOption option, OptionData optiondata, int steps):
  cdef double rate = optiondata.rate
  cdef double spot = optiondata.spot
  cdef double volatility = optiondata.volatility
  cdef double dividend = optiondata.dividend
  cdef double expiry = option.expiry
  cdef double H = expiry / (<float>steps)

  cdef double up = cexp(((rate - dividend) * H) + volatility * csqrt(H))
  cdef double down = cexp(((rate - dividend) * H) - volatility * csqrt(H))  
  cdef double prob_up = (cexp((rate - dividend) * H) - down) / (up - down)
  cdef double prob_down = 1 - prob_up

  cdef double spot_t = 0.00
  cdef double payoff_t = 0.00
  cdef unsigned int numNodes = steps + 1
  cdef unsigned int i

    
  for i in range(numNodes):
    spot_t = spot * (up ** (steps - i)) * (down ** i)
    payoff_t += option.payoff(spot_t) * binom.pmf(steps - i, steps, prob_up)
  price = payoff_t * cexp(-rate * expiry)

  return price


cdef double AmericanBinomialPricer(VanillaOption option, OptionData optiondata, int steps):
  cdef double rate = optiondata.rate
  cdef double spot = optiondata.spot
  cdef double volatility = optiondata.volatility
  cdef double dividend = optiondata.dividend
  cdef double expiry = option.expiry
  cdef double H = expiry / (<float>steps)

  cdef double up = cexp(((rate - dividend) * H) + volatility * csqrt(H))
  cdef double down = cexp(((rate - dividend) * H) - volatility * csqrt(H))  
  cdef double prob_up = (cexp((rate - dividend) * H) - down) / (up - down)
  cdef double prob_down = 1 - prob_up
  cdef double disc = cexp(-rate * H)
  cdef double dpu = disc * prob_up
  cdef double dpd = disc * prob_down

  cdef unsigned int numNodes = steps + 1
  cdef double[:] call_t = np.empty(numNodes, dtypes=np.float64)
  cdef double[:] spot_t = np.empty(numNodes, dtypes=np.float64)
  cdef unsigned int i
  cdef unsigned int j

  for i in range(numNodes):
    spot_t[i] = spot * (up ** (steps - i)) * (down ** i)
    call_t[i] = option.payoff(spot_t[i])

  for i in range((steps - 1), -1, -1):
    for j in range(i+1):
      call_t[j] = dpu * call_t[j] + dpd * call_t[j+1]
      spot_t[j] = spot_t[j] / up
      call_t[j] = max(call_t[j], option.payoff(spot_t[j]))

  return call_t[0]


cdef double NaiveMonteCarloPricer(VanillaOption option, OptionData optiondata, int replications, int time_steps):
  cdef double rate = optiondata.rate
  cdef double spot = optiondata.spot
  cdef double volatility = optiondata.volatility
  cdef double dividend = optiondata.dividend
  cdef double expiry = option.expiry
  cdef double H = expiry / (<float>time_steps)

  cdef double [:] z = np.random.normal(size = replications)
  cdef double [:] spot_t = spot * cexp((rate - dividend - 0.5 * volatility * volatility) * H + volatility * csqrt(H) * z)
  cdef double [:] payoff_t = option.payoff(spot_t)

  cdef double [:] price = payoff_t.mean() * cexp(-rate * H)

  return price