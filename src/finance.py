
class Finance():
    
    def __init__(self, **kwargs):
        self.precision = kwargs['precision'] if 'precision' in kwargs else 2

    
    def pv(self, *args, **kwargs):
        """ 
        Calculates the present value.
        pv(amount, rate = 0.05, timeframe = 15) 
        """
        return round((args[0] / (1 + kwargs['rate']) ** kwargs['timeframe']), self.precision)


    def fv(self, *args, **kwargs):
        """
        Calculates the future value.
        fv(amount, rate = 0.05, timeframe = 15)
        """
        return round((args[0] * (1 + kwargs['rate']) ** kwargs['timeframe']), self.precision)

    
    def cagr(self, *args, **kwargs):
        """
        Calculates the CAGR (compound annual growth rate)
        cagr(current_amount, future_amount, timeframe = 15)
        """
        return round((((args[1] / args[0]) ** (1 / kwargs['timeframe'])) - 1), self.precision)


    def mortgage_payment(self, *args, **kwargs):
        """
        Calculates the mortgage payment.
        mortgage_payment(amount, rate = 0.05, timeframe = 15)
        """
        monthly_rate = kwargs['rate'] / 12 
        return round(((monthly_rate / (1 - (1 + monthly_rate) ** (-kwargs['timeframe'] * 12))) * args[0]), self.precision)




