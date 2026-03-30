"""
Utility function to check whether a number is prime.
"""


def is_prime(number: int) -> bool:
    """Check if a given integer is a prime number.

    A prime number is a natural number greater than 1 that has no positive
    divisors other than 1 and itself.

    Args:
        number: The integer to check.

    Returns:
        True if the number is prime, False otherwise.
    """
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True
