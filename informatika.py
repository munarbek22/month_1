from random import random, randint

# number 1Дан массив из 20 элементов. Первые 5 элементов упорядочить по убыванию, последние
# 5 – по возрастанию
# arr = [randint(1, 100) for _ in range(20)]
#
# print("Исходный массив:")
# print(arr)
#
# # Первые 5 элементов упорядочить по убыванию
# arr[:5] = sorted(arr[:5], reverse=True)
#
# # Последние 5 элементов упорядочить по возрастанию
# arr[-5:] = sorted(arr[-5:])
#
# print("\nМассив после изменений:")
# print(arr)

# number 2Дан массив из 15 элементов (числа от -5 до 5). Отсортировать массив по возрастанию,
# убрав нули влево.
# a = [0, -3, -1, 0, 15, 1, 2, 3, 4, -5, 0]
# # print(a)
# # zeros = [0] * a.count(0)
# # non_zeros = []
# # for x in a:
# #     if x != 0:
# #         non_zeros.append(x)
# #         sorted(non_zeros)
# #
# # b = zeros + non_zeros
# # print(b)


# # # number 3Дан массив из 10 элементов (числа от 20 до 50). Отсортировать список по сумме цифр в
# числе
# import random
#
# # Создаем массив из 10 случайных чисел в диапазоне от 20 до 50
# arr = [random.randint(20, 50) for _ in range(10)]
#
# print("Исходный массив:")
# print(arr)
#
# # Функция для вычисления суммы цифр числа
# def sum_of_digits(num):
#     return sum(int(digit) for digit in str(num))
#
# # Сортируем массив по сумме цифр в числе
# sorted_arr = sorted(arr, key=sum_of_digits)
#
# print("\nМассив после сортировки по сумме цифр:")
# print(sorted_arr)
# transformed_arr = [sum_of_digits(x) for x in arr]
# # Сортируем массив
# sorted_transformed = sorted(transformed_arr)
#
# print("\nМассив с заменой чисел на суммы цифр и сортировкой:")
# print(sorted_transformed)

# №4Дан массив из 20 элементов. Четные числа упорядочить по убыванию, нечетные – по
# возрастанию.
# arr = [randint(0, 100) for _ in range(20)]
# print(arr)
# chet = sorted([x for x in arr if x % 2 == 0], reverse=True)
# nechet = sorted([i for i in arr if i % 2 != 0], )
#
# print(nechet)
# print(chet)

# №5Дан массив из 10 элементов (числа от 10 до 30). Найти среднее арифметическое этого
# массива и отсортировать по убыванию все элементы, большие среднего
# arr = [randint(10, 30) for _ in range(10)]
#
# print(arr)
# lenght = len(arr)
# print(lenght)
# for i in arr:
#     if i:
#         average = sum(arr)/lenght
# print(average)
# for x in arr:
#     if x > average:
#         print(x)

# №6Дан массив из 15 элементов. Первые 4 элемента упорядочить по возрастанию,
# последние 4 – по убыванию

# arr = [randint(0, 100) for _ in range(15)]
# print(arr)
# arr_2 = sorted(arr[:4])
# print(arr_2)
# arr_3 = sorted(arr[-4:], reverse=True)
# print(arr_3)

# №7Дан массив из 10 элементов (числа от -5 до 5). Отсортировать массив по возрастанию,
# убрав цифры -5 вправо.
# Исходный массив
# arr = [0, -5, 3, -2, -5, 1, -4, 5, -5, 2]
# print(arr)
# filtered = []
# for i in arr:
#     if i != -5:
#         filtered.append(i)
# f = sorted(filtered)
#
# final_arr = f + [-5] * arr.count(-5)
# print(final_arr)



# №8Дан массив из 10 элементов (числа от 0 до 20). Числа, стоящие на нечетных номерах,
# отсортировать по убыванию.
# Исходный массив
# arr = [12, 7, 9, 14, 5, 16, 3, 11, 8, 17]
# print(arr)

# Извлекаем элементы на нечетных индексах
# odd_indices_elements = arr[1::2]

# Сортируем эти элементы по убыванию
# odd_indices_elements.sort(reverse=True)

# Вставляем отсортированные элементы обратно на их места
# arr[1::2] = odd_indices_elements
# a.append(odd_indices_elements)

# print(odd_indices_elements)

# №9Дан массив из 10 элементов (числа от -2 до 6). Отсортировать массив по убыванию,
# убрав цифры 0 вправо
# arr = [-2, 0, 1, 3, 0, 5, 6, 0, 3, 0,]
# print(arr)
#
# filtered = []
# for i in arr:
#     if i != 0:
#         filtered.append(i)
# arr_2 = sorted(filtered, reverse=True)
# final_arr = filtered + [0] * arr.count(0)
# print(final_arr)

# number Дан массив из 10 элементов (числа от 0 до 5). Удалить повторяющиеся элементы из
# списка, окончательный список отсортировать по возрастанию
# arr = [2, 0, 1, 3, 0, 5, 3, 0, 3, 0]
# print(arr)
# way 1
# arr_2 = sorted(set(arr))
# print(arr_2)
# way 2
# arr_2 = []
# for i in arr:
#     if i not in arr_2:
#         arr_2.append(i)
# arr_2.sort()
# print(arr_2)
# 10. Дан массив из 10 элементов (числа от 20 до 50). Отсортировать список по возрастанию
# последней цифры в числе.
# arr = [randint(20, 50) for _ in range(10)]
# print(arr)
# def last_digit(num):
#     return num % 10
#
# arr_2 = sorted(arr, key=last_digit)
# print(arr_2)

# 11. Дан массив из 10 элементов (числа от 10 до 50). Отсортировать список по убыванию
# первой цифры в числе.
# arr = [randint(20, 50) for _ in range(10)]
# print(arr)
# def get_digit(num):
#     return int(str(num)[0])
# arr_2 = sorted(arr, key=get_digit, reverse=True)
# print(arr_2)

# 12. Дан массив из 20 элементов. Числа, кратные 3, упорядочить по возрастанию, кратные 7
# – по убыванию.
# arr = [randint(0,100) for _ in range(20)]
# print(f'первоначальный массив: {arr}')
# arr_for3 = []
# arr_for7 = []
# just_nums = []
# for i in arr:
#     if i % 3 == 0:
#         arr_for3.append(i)
#     elif i % 7 == 0:
#         arr_for7.append(i)
#     else:
#         just_nums.append(i)
# print(f'числа кратные 3:{arr_for3}')
# print(f'числа кратные 7:{arr_for7}')
# final_arr = sorted(arr_for3) + sorted(arr_for7, reverse=True) + just_nums
# print(final_arr)

# Дан массив из 10 элементов (числа от 10 до 30). Отсортировать список по
# произведению цифр в числе.
arr = [randint(10,30) for _ in range(10)]
print(arr)
# def first_digit(num):
#     return int(str(num)[0]) * int(num % 10)
# arr_2 = sorted(arr, key=first_digit)
# print(arr_2)
products = []
for num in arr:
    desyatki = num // 10
    edinicy = num % 10
    product = desyatki * edinicy
    products.append((num, product))  # Сохраняем пару (число, произведение)

# Сортируем пары по произведению
products.sort(key=lambda x: x[1])  # Сортируем по второму элементу в паре

# Извлекаем числа из отсортированного списка
sorted_arr = [item[0] for item in products]

print("Отсортированный массив:", sorted_arr)


# Дан массив из 10 элементов (числа от 20 до 50). Найти среднее арифметическое этого
# массива и отсортировать по возрастанию все элементы, меньшие среднего.
# arr = [randint(20, 50) for _ in range(10)]
# print(arr)
# average =  sum(arr) / len(arr)
# print(average)
# arr_2 = []
# for i in arr:
#     if i < average:
#         arr_2.append(i)
# s = sorted(arr_2)
# print(s)

# 15. Дан массив из 20 элементов (числа от -10 до 10). Все отрицательные числа
# отсортировать по возрастанию, положительные – по убыванию.
# arr = list(range(-10, 10))
# print(arr)
# otric = []
# polog = []
# for i in arr:
#     if i < 0:
#         otric.append(i)
#     elif i >= 0:
#         polog.append(i)
# final_arr = sorted(otric) + sorted(polog, reverse=True)
# print(final_arr)

# 16. Дан массив из 10 элементов (числа от 0 до 20). Числа, стоящие на четных номерах,
# отсортировать по возрастанию.
# arr = [randint(0, 20) for _ in range(10)]
# print(arr)
# chet = sorted(arr[::2])
# print(chet)

# Дан массив из 10 элементов (числа от 10 до 30). Отсортировать список по разнице цифр
# в числе
# arr = [randint(10, 30) for _ in range(10)]
# print(arr)
# def get_digits(num):
#     return int(str(num)[0]) - int(str(num)[1])
# arr_2 = sorted(arr, key=get_digits)
# print(arr_2)

