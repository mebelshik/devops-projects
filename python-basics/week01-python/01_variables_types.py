"""
Week 01: Variables and Data Types
Тема: Переменные и типы данных в Python
"""

# 1. ПЕРЕМЕННЫЕ И ТИПЫ ДАННЫХ

# Integer (целые числа)
age = 25
print(f"age = {age}, type = {type(age)}")

# Float (вещественные числа)
height = 1.75
print(f"height = {height}, type = {type(height)}")

# String (строки)
name = "Vladimir"
print(f"name = {name}, type = {type(name)}")

# Boolean (логические значения)
is_student = True
print(f"is_student = {is_student}, type = {type(is_student)}")

# List (список)
numbers = [1, 2, 3, 4, 5]
print(f"numbers = {numbers}, type = {type(numbers)}")

# Dictionary (словарь)
person = {"name": "Vladimir", "age": 25, "city": "Moscow"}
print(f"person = {person}, type = {type(person)}")

# Tuple (кортеж - неизменяемый список)
coordinates = (10.5, 20.3)
print(f"coordinates = {coordinates}, type = {type(coordinates)}")

# Set (множество)
unique_numbers = {1, 2, 3, 4, 5}
print(f"unique_numbers = {unique_numbers}, type = {type(unique_numbers)}")

# 2. ПРЕОБРАЗОВАНИЕ ТИПОВ

print("\n=== Type Conversion ===")
str_number = "42"
int_number = int(str_number)
print(f"'{str_number}' as int = {int_number}")

float_from_int = float(int_number)
print(f"{int_number} as float = {float_from_int}")

# 3. ПРАКТИКА

# Задание 1: Создай переменные для своих данных
my_name = "TODO"  # Замени на своё имя
my_age = 0  # Замени на свой возраст
my_height = 0.0  # Замени на свой рост

print(f"\nМои данные: {my_name}, {my_age} лет, {my_height}м")

# Задание 2: Работа с collections
my_hobbies = ["TODO", "TODO", "TODO"]  # Добавь свои хобби
print(f"Мои хобби: {my_hobbies}")
