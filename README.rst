# python-finance - Simple package for finance calculations I always forget  

# Usage 

from finance import Finance 
f = Finance(precision = 2)

## find the present value
f.pv(amount, rate = 0.05, timeframe = 15) 

## find the future value 
f.fv(amount, rate = 0.05, timeframe = 15)

## find the mortgage payment 
f.mortgage_payment(finance_amount, rate = 0.05, timeframe = 15) 

## find the cagr (compound annual growth rate)
f = Finance(precision = 3)
f.cagr(current_amount, future_amount, timeframe = 15)


# Tests

pytest 

