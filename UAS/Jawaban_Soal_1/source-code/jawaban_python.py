# Function
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

# Recursive
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))
