# test_calculator.py

from testify import TestCase, assert_equal, assert_raises, run

# Import the Calculator class from calculator.py
from calculator import Calculator

class CalculatorTestCase(TestCase):

    def test_addition(self):
        calc = Calculator()
        result = calc.add(3, 5)
        assert_equal(result, 8)

    def test_subtraction(self):
        calc = Calculator()
        result = calc.subtract(10, 4)
        assert_equal(result, 6)

    def test_multiplication(self):
        calc = Calculator()
        result = calc.multiply(2, 6)
        assert_equal(result, 12)

    def test_division(self):
        calc = Calculator()
        result = calc.divide(15, 3)
        assert_equal(result, 5)

    def test_division_by_zero(self):
        calc = Calculator()
        # Test that dividing by zero raises a ValueError
        with assert_raises(ValueError):
            calc.divide(10, 0)

if __name__ == '__main__':
    run()
