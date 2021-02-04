import unittest
import calculator

class TestCaseCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.calc.add(10, 1), 11)
        self.assertEqual(calculator.calc.add(50, 50), 100)
    def test_sub(self):
        self.assertEqual(calculator.calc.sub(10, 1), 9)
        self.assertEqual(calculator.calc.sub(100, 50), 50)
    def test_multi(self):
        self.assertEqual(calculator.calc.multi(10, 5), 50)
        self.assertEqual(calculator.calc.multi(1, 10), 10)
    def test_divi(self):
        self.assertEqual(calculator.calc.divi(10, 5), 2)
        self.assertIsNone(calculator.calc.divi(10, 0))

if __name__ == "__main__":
    unittest.main()
