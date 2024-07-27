def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except TypeError:
        return "Error: Invalid input type. Please provide numbers."
    else:
        return result
    finally:
        print("Execution completed.")

# Contoh penggunaan
print(divide(10, 2))  # Output: 5.0
print(divide(10, 0))  # Output: Error: Division by zero is not allowed.
print(divide(10, 'a'))  # Output: Error: Invalid input type. Please provide numbers.
