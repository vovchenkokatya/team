def factorial_recursive(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

print(f"Факторіал 5 (рекурсивно): {factorial_recursive(5)}")
