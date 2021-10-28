"""Напишите программу, которая считывает целое число и выводит текст,
аналогичный приведенному в примере
(важно в точности соблюдать вывод программы:
обратите внимание на пробелы и на точки).
Нельзя пользоваться конкатенацией строк,
используйте print с несколькими параметрами.
Формат ввода
Вводится целое число (гарантируется, что число находится в диапазоне
от -1000 до +1000).
Формат вывода
Выведите две строки, согласно образцу."""
number = int(input())
leftover = number % 10
next_number = (number - leftover) + (leftover + 1)
prev_number = (number - leftover) + (leftover - 1)
# print(f"The next number for the number {number} is") # {next_number}.\n
print(f"The previous number for the number {number} is {prev_number}.")
