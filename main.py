
import math
print(math.factorial(5))

def factorial_loop(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(f"Факторіал 5 дорівнює: {factorial_loop(5)}")

