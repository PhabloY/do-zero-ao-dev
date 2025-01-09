def divide(n, d):
    try:
        return n / d
    except ZeroDivisionError:
        return n

print(divide(8, 0))