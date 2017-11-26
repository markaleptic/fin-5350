class OptionData(object):
    def __init__(self, rate, spot, volatility, dividend):
        self.rate = rate
        self.spot = spot
        self.volatility = volatility
        self.dividend = dividend
    # TODO - Define individual set methods

    def get_data(self):
        return self.rate, self.spot, self.volatility, self.dividend

    def get_rate(self):
        return self.rate

    def get_spot(self):
        return self.spot

    def get_volatility(self):
        return self.volatility

    def get_dividend(self):
        return self.dividend

