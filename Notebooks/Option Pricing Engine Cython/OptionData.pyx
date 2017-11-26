cdef class OptionData:
  def __init__(self, rate, spot, volatility, dividend):
    self._rate = rate
    self._spot = spot
    self._volatility = volatility
    self._dividend = dividend
    
  property rate:
    def __get__(self):
      return self._rate

    def __set__(self, rate):
      self._rate = rate

  property spot:
    def __get__(self):
      return self._spot

    def __set__(self, spot):
      self._spot = spot

  property volatility:
    def __get__(self):
      return self._volatility

    def __set__(self, volatility):
      self._volatility = volatility

  property dividend:
    def __get__(self):
      return self._dividend

    def __set__(self, dividend):
      self._dividend = dividend