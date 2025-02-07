def factorial(n):
    """Returns the factorial of a number using recursion."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Taking user input
num = int(input("Enter a number: "))

# Checking for negative input
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"The factorial of {num} is {factorial(num)}")
