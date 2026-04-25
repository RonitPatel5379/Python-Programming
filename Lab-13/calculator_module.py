def add(x, y):
    """Adds two numbers."""
    return x + y

def sub(x, y):
    """Subtracts the second number from the first."""
    return x - y

def mul(x, y):
    """Multiplies two numbers."""
    return x * y

def div(x, y):
    """Divides the first number by the second. Handles division by zero."""
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y
