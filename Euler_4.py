"""
Задача 4    Наибольшее произведение-палиндром

Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково.
Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.

Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.

====================================
Problem 4.       Largest palindrome product.

A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
import time


start = time.time()

lst = set()
for i in range(100, 1000):
    for j in range(100, 1000):
        lst.add(i * j)
lst = list(lst)
lst.sort(reverse=True)

k = 0
number = str(lst[k])
# Установливаю - сколько первых паллиндромов вывести на печать
for _ in range(3):
    while number[:3] != number[:2:-1]:
        k += 1
        number = str(lst[k])
    print(lst[k])
    k += 1
    number = str(lst[k])

# Время исполнения скрипта
print(time.time() - start)
