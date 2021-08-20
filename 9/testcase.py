import unittest
from Fibonacci import Fibonacci

class FibonacciTest(unittest.TestCase):
    def test_fib_neg1(self):
        self.assertRaises(TypeError, Fibonacci(-1), True)
        self.assertAlmostEqual(Fibonacci(-1),8)
        self.assertRaises(TypeError, Fibonacci(-1), True) 
    
    def test_fib_31(self):
        self.assertRaises(TypeError, Fibonacci(31), True)
        self.assertAlmostEqual(Fibonacci(31),None)
        self.assertRaises(TypeError, Fibonacci(31), True) 

if __name__ == "__main__":
    unittest.main(argv=[''],verbosity=2, exit=False)