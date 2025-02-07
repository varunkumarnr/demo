def is_prime(n):
    """Returns True if n is a prime number, otherwise False."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Taking user input
num = int(input("Enter a number: "))

# Checking and displaying result
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
    
