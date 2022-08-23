import pandas as pd 


class Finance():

    
    def __init__(self, **kwargs):
        self.precision = kwargs['precision'] if 'precision' in kwargs else 2
        self.money = None

    
    def pv(self, *args, **kwargs):
        """ 
        Calculates the present value.
        pv(amount, rate = 0.05, timeframe = 15, str = False) 
        """
        v = round((args[0] / (1 + kwargs['rate']) ** kwargs['timeframe']), self.precision)
        if 'str' in kwargs and kwargs['str']:
            return self.as_str(v)
        else: 
            return v


    def fv(self, *args, **kwargs):
        """
        Calculates the future value.
        fv(amount, rate = 0.05, timeframe = 15, str = False)
        """
        v = round((args[0] * (1 + kwargs['rate']) ** kwargs['timeframe']), self.precision)
        if 'str' in kwargs and kwargs['str']:
            return self.as_str(v)
        else:
            return v
    
    def cagr(self, *args, **kwargs):
        """
        Calculates the CAGR (compound annual growth rate)
        cagr(current_amount, future_amount, timeframe = 15)
        """
        return round((((args[1] / args[0]) ** (1 / kwargs['timeframe'])) - 1), self.precision)


    def mortgage_payment(self, *args, **kwargs):
        """
        Calculates the mortgage payment.
        mortgage_payment(amount, rate = 0.05, timeframe = 15, str = False)
        """
        monthly_rate = kwargs['rate'] / 12 
        v = round(((monthly_rate / (1 - (1 + monthly_rate) ** (-kwargs['timeframe'] * 12))) * args[0]), self.precision)
        if 'str' in kwargs and kwargs['str']:
            return self.as_str(v)
        else:
            return v


    def analysis(self, amount, years = 20, savings = 10_000, savings_years = 10, rate = 0.05):
        """
        Analyze future values per year w/ savings 
        analysis(amount, savings = 10_000, years = 10, rate = 0.05):
        """
        amt = amount
        acc = []
        for i in range(years):
            fv = self.fv(amt, rate = rate, timeframe = 1)
            if i < savings_years:
                amt = fv + savings 
            else: 
                amt = fv

            acc.append({'year': i, 'fv': fv, 'amt': amt})

        df = pd.DataFrame(acc)
        df = df.set_index('year')
        return df

            


    def as_str(self, n):
        return "$ {:,.2f}".format(n)



