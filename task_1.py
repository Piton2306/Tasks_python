"""Задание 1.
Сумма всех простых чисел, не превышающих X.
Язык программирования Python."""

from math import sqrt

num = int(input('Введите число:'))
prime_numbers_sum = 0
for i in range(2, num + 1):
    isPrime = True
    for j in range(2, int(sqrt(i)) + 1):
        if i % j == 0:
            isPrime = False
            break
    if isPrime:
        prime_numbers_sum += i
print(prime_numbers_sum)
