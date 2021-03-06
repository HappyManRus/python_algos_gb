"""
Задание 5.*

Приведен наивный алгоритм нахождения i-го по счёту
простого числа (через перебор делителей).

Попробуйте решить эту же задачу,
применив алгоритм "Решето эратосфена" (https://younglinux.info/algorithm/sieve)

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма
"""
from timeit import timeit
import math


def simple(i):
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n


def resheto(n):
    if n > 10:
        koef = n // int(math.log10(n))
    else:
        koef = n
    arrsize = n * koef
    arr = list([i for i in range(arrsize + 1)])
    i = 2
    k = 0
    while (k < n) and (i <= arrsize):
        if arr[i] != 0:
            k += 1
            j = i + i
            while j <= arrsize:
                arr[j] = 0
                j = j + i
        i += 1
    return arr[i - 1]


i = int(input('Введите порядковый номер искомого простого числа: '))
print(simple(i))
print(resheto(i))

print(
    timeit(
        'simple(i)',
        setup='from __main__ import simple, i',
        number=1))

print(
    timeit(
        'resheto(i)',
        setup='from __main__ import resheto, i',
        number=1))

# Сам принцип Решето Эратосфена понял, и он действительно эффективнее даже на малых числах.
# Но в моем коде огромный минус - избыточность массива. И сама зависимость от массива смущает.
# Думаю есть способы обойтись без массива. Любо более четко расчитать размерность массива.
# Очевидно что с ростом номера искомого числа, размерность массива пропорционально уменьшается, начиная с n*n, до n*(n // x) и так далее.
# Пока не могу придумать. Взял логорифм10, так вроде на разных диапозонах работает.

# Введите порядковый номер искомого простого числа: 3478
# 32411
# 32411
# 17.4371879
# 3.597511500000003

# Введите  порядковый номер искомого простого числа: 10
# 29
# 29
# 4.7499999999978115e-05
# 4.6700000000177155e-05
