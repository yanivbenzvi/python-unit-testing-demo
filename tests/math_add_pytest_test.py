# Test case 1
from src.math import add


def test_add_positive_numbers():
    assert add(3, 4) == 7


# Test case 2
def test_add_negative_numbers():
    assert add(-3, -4) == -7


# Test case 3
def test_add_mixed_numbers():
    assert add(2, -5) == -3
