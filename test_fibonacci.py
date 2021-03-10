import unittest
import fibonacci

class TestCaseCalc(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(fibonacci.fib(0), 0)
        self.assertEqual(fibonacci.fib(1), 1)
        self.assertEqual(fibonacci.fib(2), 2)
        self.assertEqual(fibonacci.fib(3), 3)
        self.assertEqual(fibonacci.fib(5), 8)

if __name__ == "__main__":
    unittest.main()
