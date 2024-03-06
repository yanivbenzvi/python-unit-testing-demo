# Test case 1: Given positive numbers, when dividing them, then the result should be correct
from src.math import divide
import pytest


def test_divide_positive_numbers():
    # Given
    dividend = 10
    divisor = 2

    # When
    result = divide(dividend, divisor)

    # Then
    assert result == 5


# Test case 2: Given a negative dividend and a positive divisor, when dividing them, then the result should be negative
def test_divide_negative_dividend_positive_divisor():
    # Given
    dividend = -10
    divisor = 2

    # When
    result = divide(dividend, divisor)

    # Then
    assert result == -5


# Test case 3: Given a zero dividend and a non-zero divisor, when dividing them, then the result should be zero
def test_divide_zero_dividend():
    # Given
    dividend = 0
    divisor = 5

    # When
    result = divide(dividend, divisor)

    # Then
    assert result == 0


# Test case 4: Given a non-zero dividend and a zero divisor, then it should raise a ValueError
def test_divide_by_zero():
    # Given
    dividend = 10
    divisor = 0

    # When, Then
    with pytest.raises(ValueError):
        divide(dividend, divisor)
