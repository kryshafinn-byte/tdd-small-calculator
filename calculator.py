def add(a, b):
    """Return the answer of the two digits."""
    return a + b

def subtract(a, b):
    """Return the answer of the two digits."""
    return a - b


def multiply(a, b):
    """Return the answer of the two digits."""
    return a * b

def divide(a, b):
    """Return the answer of two digits. If b is zero, show an error."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def run_pytest():
    print("Running calculator tests...")

    assert add(100, 3) == 103
    assert subtract(1000, 4) == 996
    assert multiply(10000, 5) == 50000
    assert divide(600000, 6) == 100000
    print("All tests made it!\n")


if __name__ == "__main__":
    run_pytest()
