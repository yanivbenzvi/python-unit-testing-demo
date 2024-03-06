# Function to be tested
def add(a, b):
    return a + b


# Function to be tested
def divide(dividend, divisor):
    if divisor == 0:
        raise ValueError("Cannot divide by zero")
    return dividend / divisor


class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b
