"""Пирожок в столовой стоит A рублей и B копеек.
Определите,
сколько рублей и копеек нужно заплатить за N пирожков.
Формат ввода
Программа получает на вход три числа:
A, B, N —  целые, неотрицательные, не превышают 10000.
Формат вывода
Программа должна вывести два числа:
стоимость покупки в рублях и копейках."""
a = int(input())
b = int(input())
c = int(input())
total = ((a * c) * 100) + (b * c)
coins = total % (10 ** 2)
grn = total // 100
print(grn, coins)
