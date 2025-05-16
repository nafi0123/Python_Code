def count_divisors(n):
    divisor = 0
    for i in range(1, int(n**0.5) + 1):
        if i * i == n:
            divisor += 1  # Perfect square case
        elif n % i == 0:
            divisor += 2  # i and n // i are both divisors
    return divisor

# Example usage
number = 24
print(f"Number of divisors of {number}: {count_divisors(number)}")
