def is_prime(n):
    """Check if a number is a prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def calculate_fibonacci(n):
    """Calculate the n-th Fibonacci number."""
    if n < 0:
        raise ValueError("Fibonacci number is not defined for negative integers.")
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def sum_of_all_fibonacci(n):
    """Calculate the sum of the first n Fibonacci numbers."""
    if n < 0:
        raise ValueError("Sum of Fibonacci numbers is not defined for negative integers.")
    total = 0
    for i in range(n + 1):
        total += calculate_fibonacci(i)
    return total
