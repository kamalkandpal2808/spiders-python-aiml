"""Function definitions, arguments, and return values."""


def greet(name):
    """Return a greeting for name."""
    return f"Hello, {name}!"


def is_prime(number):
    """Return True when number is prime."""
    if number < 2:
        return False
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True


def factorial(number):
    """Calculate factorial for a non-negative integer."""
    if number < 0:
        raise ValueError("Factorial is not defined here for negative integers.")
    result = 1
    for value in range(2, number + 1):
        result *= value
    return result


if __name__ == "__main__":
    print(greet("Python programmer"))
    print("Is 17 prime?", is_prime(17))
    print("6! =", factorial(6))
