def function(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0  # Or handle it appropriately, e.g., raise a custom exception, return a default value, etc.

result = function(10, 0)
print(result)  # Output: 0