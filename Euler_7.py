"""
Задача 7    10001-ое простое число

Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13.
Очевидно, что 6-ое простое число - 13.

Какое число является 10001-ым простым числом?

"""
import time


def isprime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n


i = 2
number = 0
start = time.time()
while number <= 10000:
    if isprime(i):
        number += 1
    i += 1
print(i - 1, number)
print(time.time() - start)

"""
# List of 10 prime numbers
n = []
i = 2
num = 0
while num <= 10:
    if isprime(i):
        n.append(i)
        num += 1
    i += 1
print(n)
"""
