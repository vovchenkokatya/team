
def calculate_area(width, height):
    return width * height

# Виклик функції
result = calculate_area(5, 10)
print(f"Площа прямокутника: {result}")

def factorial_recursive(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

print(f"Факторіал 5 (рекурсивно): {factorial_recursive(5)}")
