"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""
from random import randint

def guessNum(n=1):
    if n>10:
        print("Вы 10 раз не смогли угадать. Число которые вы пытались угадать = ", secretNum)
        return 0
    try:
        print("Попытка № ",n)
        answer = int(input("Угадайте число от 0 до 100: "))
        if answer != secretNum:
            if answer < secretNum:
                print ("Не угадали, число должно быть больше!")
            else:
                print("Не угадали, число должно быть меньше!")
            return guessNum(n + 1)
        else:
            print("Гениально, угадали! Поздравляю!")
            return 0
    except ValueError:
        print("Введенные данные не являются целым числом.")
        return guessNum(n + 1)


secretNum = randint(0, 100)
guessNum()