from libc.math cimport exp as cexp
from libc.math cimport sqrt as csqrt

import numpy as np
cimport numpy as np

from scipy.stats import binom
from OptionData cimport OptionData

cdef class VanillaOption:
  cdef double _strike
  cdef double _expiry

  cpdef payoff(self, double spot)

cdef class VanillaCallOption:
  cpdef payoff(self, double spot)

cdef class VanillaPutOption:
  cpdef payoff(self, double spot)

cdef double EuropeanBinomialPricer(VanillaOption option, OptionData optiondata, int steps)
cdef double AmericanBinomialPricer(VanillaOption option, OptionData optiondata, int steps)
cdef double NaiveMonteCarloPricer(VanillaOption option, OptionData optiondata, int replications, int time_steps)