"""
Week 01: Operators and Conditionals
Тема: Операторы и условные операторы
"""

# 1. АРИФМЕТИЧЕСКИЕ ОПЕРАТОРЫ

print("=== Arithmetic Operators ===")
a = 10
b = 3

print(f"{a} + {b} = {a + b}")  # Сложение
print(f"{a} - {b} = {a - b}")  # Вычитание
print(f"{a} * {b} = {a * b}")  # Умножение
print(f"{a} / {b} = {a / b}")  # Деление
print(f"{a} // {b} = {a // b}")  # Целое деление
print(f"{a} % {b} = {a % b}")  # Остаток
print(f"{a} ** {b} = {a ** b}")  # Возведение в степень

# 2. ОПЕРАТОРЫ СРАВНЕНИЯ

print("\n=== Comparison Operators ===")
x = 5
y = 5

print(f"{x} == {y}: {x == y}")  # Равно
print(f"{x} != {y}: {x != y}")  # Не равно
print(f"{x} > {y}: {x > y}")   # Больше
print(f"{x} < {y}: {x < y}")   # Меньше
print(f"{x} >= {y}: {x >= y}") # Больше или равно
print(f"{x} <= {y}: {x <= y}") # Меньше или равно

# 3. ЛОГИЧЕСКИЕ ОПЕРАТОРЫ

print("\n=== Logical Operators ===")
p = True
q = False

print(f"{p} and {q} = {p and q}")  # И (оба должны быть True)
print(f"{p} or {q} = {p or q}")    # Или (хотя бы один True)
print(f"not {p} = {not p}")        # Не (инверсия)

# 4. УСЛОВНЫЕ ОПЕРАТОРЫ (if/elif/else)

print("\n=== Conditionals ===")

# if/else
age = 18
if age >= 18:
    print("Ты совершеннолетний")
else:
    print("Ты несовершеннолетний")

# if/elif/else
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
print(f"Твоя оценка: {grade}")

# Ternary operator (одна строка)
status = "Pass" if score >= 70 else "Fail"
print(f"Статус: {status}")

# 5. ПРАКТИКА

print("\n=== Практика ===")

# Задание 1: Проверь чётность числа
number = 7
if number % 2 == 0:
    print(f"{number} - чётное число")
else:
    print(f"{number} - нечётное число")

# Задание 2: Проверь сезон по месяцу
month = 3  # Замени на свой месяц
if month in [12, 1, 2]:
    season = "Winter"
elif month in [3, 4, 5]:
    season = "Spring"
elif month in [6, 7, 8]:
    season = "Summer"
else:
    season = "Autumn"
print(f"Месяц {month} - это {season}")

# Задание 3: Проверь диапазон
num = 25
if 0 <= num <= 100:
    print(f"{num} в диапазоне 0-100")
else:
    print(f"{num} вне диапазона")
