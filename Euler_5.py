"""
Задача 5    Наименьшее кратное

2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.

Какое самое маленькое число делится нацело на все числа от 1 до 20?
===
"""
import time


def max_number(number):
    """
    Возвращает произведение уникальных делителей, входящих в список чисел

    В нашем случае это числа от 11 до 20, т.к. все остальные числа повторяются.
    Например:
    9 входит в 18: 18 = 9 * 2
    8 входит в 16: 16 = 8 * 2
    ...
    5 входит в 20, 15
    и т.д.
    Думаю, что можно доказать, что все числа от 1 до N/2 уже не являются уникальными делителями
    и являются делителями второй половины чисел.
    """
    answer = 1
    for i in range(int(number / 2) + 1, number + 1):
        print(i)
        answer *= i
    print('max number =', answer)
    return answer


def my_func(number, answer):
    for i in range(number, answer, 2):
        if i % 20 == 0:
            if i % 19 == 0:
                if i % 18 == 0:
                    if i % 17 == 0:
                        if i % 16 == 0:
                            if i % 15 == 0:
                                if i % 14 == 0:
                                    if i % 13 == 0:
                                        if i % 12 == 0:
                                            if i % 11 == 0:
                                                print(i)
                                                break


def code_chezhiiyan():
    x = 20
    list1 = [100000000000]

    for x in range(20, 1000000000):
        for y in range(11, 21):
            if x % y == 0:
                if y == 20:
                    list1.append(x)
                continue
            else:
                x = x + 20
                break
        if len(list1) == 2:
            break
    print(min(list1))


start = time.time()

number = 20
answer = 670442572800
max_number(number)

my_func(number, answer)             # time =  33 сек
code_chezhiiyan()                   # time = 251 сек = 3 мин 11 сек


print(time.time() - start)


# end = 3628800
#           670 442 572 800     10E-12      единицы триллионов
# 2 432 902 008 176 640 000     10E-18      миллионы триллионов
