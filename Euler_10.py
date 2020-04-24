"""
Задача 10    Сложение простых чисел

Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.

Найдите сумму всех простых чисел меньше двух миллионов.

"""


def isprime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n


n = []
i = 2
num = 0
sum_prime = 0
while i <= 2000000:
    if isprime(i):
        n.append(i)
        num += 1
        sum_prime += i
    i += 1
print(sum_prime)
