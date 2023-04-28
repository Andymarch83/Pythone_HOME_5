'''
Задача 26:  Напишите программу, которая на вход принимает
два числа A и B, и возводит число А в целую степень B с
помощью рекурсии.

*Пример:*

A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8
'''

c = int(input('A: '))
d = int(input('B: '))


def power(a, b):
    #    res = a**b
    if b == 0:
        return 1
    else:
        return a * power(a, b - 1)


print(f'A={c}; B={d} -> {power(c, d)}')