"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321
"""

def calcTurnOver2(numCalc):
    if numCalc <= 10:
        return str(numCalc % 10)
    return str(numCalc % 10)+str(calcTurnOver2(numCalc // 10))

try:
    numforcalc = int(input("Введите целое число: "))
    print(calcTurnOver2(numforcalc))

except ValueError:
    print("Введенные данные не являются целым числом")
