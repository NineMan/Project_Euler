"""
Задача 2    Четные числа Фибоначчи

Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих.
Начиная с 1 и 2, первые 10 элементов будут:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.
"""


lst = [1]
fib1 = 1
fib2 = 1
while fib2 <= 4000000:
    fib1, fib2 = fib2, fib1 + fib2
    lst.append(fib2)

# print(lst)
a = filter(lambda x: x % 2 == 0, lst)
# print(list(a))
b = sum(a)
print('summa =', b)
