"""Напишите программу, которая по данному числу
N от 1 до 9 выводит на экран N пингвинов.
Изображение одного пингвина имеет размер 5×9 символов,
между двумя соседними пингвинами также имеется пустой (из пробелов) столбец.
Разрешается вывести пустой столбец после последнего пингвина.
Для упрощения рисования
скопируйте пингвина из примера в среду разработки.
Формат ввода
Вводится натуральное число."""
num = int(input())
my_str1 = "    _~_     "
my_str2 = "   (o o)    "
my_str3 = "  /  V  \\   "
my_str4 = " /(  _  )\\  "
my_str5 = "   ^^ ^^    "
print(my_str1 * num)
print(my_str2 * num)
print(my_str3 * num)
print(my_str4 * num)
print(my_str5 * num)
