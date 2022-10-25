# Задача 1. Найти число Пи с заданной точностью d = 0,001
# Формула Лейбница: x = 4 - 4/3 + 4/5 - 4/7 + 4/9 - ..........ряд бесконечен

# k = 1
# s = 0
# for i in range (1000000):
#     if i % 2 == 0 :
#         s += 4 / k
#     else:
#         s -= 4 / k
#     k += 2
# print(round(s, 3))

# Задача 2. Дано натуральное число N. Задать список его простых множителей

# def check_prime(check_number):
#     for j in range(2, check_number):
#         if (check_number % j == 0):
#             return False
#         else:
#             return True

# def find_primes(some_number):
#     prime_numbers = []
#     for i in range(1, some_number + 1):
#         if check_prime(i) == True:
#             if(some_number % i == 0):
#                 prime_numbers.append(i)
#     return prime_numbers

# some_number = int(input('Введите число N: '))
# print(find_primes(some_number))

# Задача 3. Задайте последовательность чисел. Выведите список неповторяющихся элементов
# Вариант а): список значений без учёта повторений [1, 1, 2, 2, 3, 5] -----> [1, 2, 3, 5]

# def unique_values(some_lst):
#     unique_values = []
#     for i in range(len(some_lst)):
#         if(unique_values.count(some_lst[i]) == 0):
#             unique_values.append(some_lst[i])
#     return unique_values


# some_list = list(map(int, input().split()))
# print(unique_values(some_list))

# Вариант б): список уникальных неповторяющихся элементов [1, 1, 2, 2, 3, 5] -----> [3,5]

# def unique_values(some_lst):
#     unique_values = []
#     for i in range(len(some_lst)):
#         # if(unique_values.count(some_lst[i]) == 0):
#         #     unique_values.append(some_lst[i])
#         if (some_lst.count(some_lst[i]) == 1):
#             unique_values.append(some_lst[i])
#     return unique_values


# some_list = list(map(int, input().split()))
# print(unique_values(some_list))

# Задача 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k

# import random

# k = int(input('Введите натуральную степень k: '))
# koeff_array = []
# for _ in range(k + 1):
#     koeff_array.append(random.randint(0, 100))
# print(koeff_array)

# indexes = {"0": "\u2070",
#            "1": "\u00B9",
#            "2": "\u00B2",
#            "3": "\u00B3",
#            "4": "\u2074",
#            "5": "\u2075",
#            "6": "\u2076",
#            "7": "\u2077",
#            "8": "\u2078",
#            "9": "\u2079",
#            }

# str = ''
# for i in range(k - 1):
#     if(i < len(koeff_array) - 2):
#         str += str(koeff_array[i]) if i != 0 else '' + str(indexes[k])
#         k -= k
# str += koeff_array[len(koeff_array) - 1]
# print(str)

# import random

# k = int(input('Введите натуральную степень k: '))
# koeffs = []
# for i in range(k + 1):
#     koeffs.append(random.randint(0, 100))
# print(koeffs)

# powers = {0: "\u2070",
#             1: "\u00B9",
#             2: "\u00B2",
#             3: "\u00B3",
#             4: "\u2074",
#             5: "\u2075",
#             6: "\u2076",
#             7: "\u2077",
#             8: "\u2078",
#             9: "\u2079",
#            }

# formula = ''
# for i in range(k - 1):
#     if(koeffs[i] != 0):
#         formula += f'{koeffs[i]}' + 'x' + powers[k] + ' + '
#     k -= 1
# if(koeffs[-1] != 0):
#     formula +=  f'{koeffs[-2]}' + 'x'
# if(koeffs[-0] != 0):
#     formula +=  ' + ' f'{koeffs[-1]}'
# print(formula)

# with open('mnogochlen.txt', 'w', encoding='utf-8') as f:
#     f.write(formula + '\n')