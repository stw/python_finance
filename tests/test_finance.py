import unittest
from src.finance import Finance

class TestFinance(unittest.TestCase):
    
    
    def setUp(self):
        self.f = Finance()

        
    def test_pv(self):
        r = self.f.pv(125_000, rate = 0.10, timeframe = 20)
        self.assertEqual(r, 18580.45, 'Present values must be equal')

    
    def test_fv(self):
        r = self.f.fv(125_000, rate = 0.10, timeframe = 20)
        self.assertEqual(r, 840937.49, 'Future values must be equal')


    def test_cagr(self):
        f = Finance(precision = 3)
        r = f.cagr(325_000, 3_000_000, timeframe = 20)
        self.assertEqual(r, 0.118, 'CAGR values must be equal')


    def test_mortgage_payment(self):
        r = self.f.mortgage_payment(400_000, rate = 0.04, timeframe = 30)
        self.assertEqual(r, 1909.66, 'Mortgage Payment values must be equal')


if __name__ == "__main__":
    unittest.main()
