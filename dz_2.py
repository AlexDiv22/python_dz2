# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму 
# его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# number = input('Введите вещественное число: ')
# amount = 0
# for i in number:
#     if i.isdigit():
#         amount += int(i)
# print(amount)


# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений 
# чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


# number = int(input('Введите число: '))
# result = [1]
# for i in range(2, number + 1):
#     result.append(result[-1] * i)
# print(result)


# 3.Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран 
# их сумму.


# n = int(input('Введите число: '))

# def sequence(n):

#     return[round((1 + 1 / x)**x, 2) for x in range (1, n + 1)]

# print(sequence(n))
# print('Сумма последовательности =', round(sum(sequence(n)), 2))


# 4.(ЕСЛИ НЕ ЗНАЕТЕ КАК ДЕЛАТЬ, МОЖНО НЕ ВЫПОЛНЯТЬ)Задайте список из N элементов, 
# заполненных числами из промежутка [-N, N]. Найдите произведение элементов на 
# указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

# from random import randint
# number = int(input('Введите число: '))
# list = []
# for i in range(number):
#     list.append(randint(-number, number))
# print(list)

# f = open('file.txt', 'w')
# while True:
#     s = input('Укажите позицию для вычисления: ')
#     if s == "":
#         break
#     f.write(s+"\n")
# f.close()

# result = 1
# f = open('file.txt', 'r')
# for line in f:
#     if line == "":
#         break
#     result *= list[int(line)]
# f.close()
# print(result)


# 5. Реализуйте алгоритм перемешивания списка.

import random
list = ['World', 1001, 'Programmer', '2022.09.25', 9.81]
for i in range(len(list)):
    index_a = random.randint(0, len(list) - 1)
    list[i], list[index_a] = list[index_a], list[i]
print(list)