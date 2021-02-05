import unittest
import calculator

class TestCaseCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(10, 1), 11)
        self.assertEqual(calculator.add(50, 50), 100)
    def test_sub(self):
        self.assertEqual(calculator.sub(10, 1), 9)
        self.assertEqual(calculator.sub(100, 50), 50)
    def test_multi(self):
        self.assertEqual(calculator.multi(10, 5), 50)
        self.assertEqual(calculator.multi(1, 10), 10)
    def test_divi(self):
        self.assertEqual(calculator.divi(10, 5), 2)
        self.assertIsNone(calculator.divi(10, 0))

if __name__ == "__main__":
    unittest.main()
