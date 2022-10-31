# Задача №1: Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint


number = int(input('Введите размер списка: '))
start_list = []
end_list = []

for i in range(number):
    start_list.append(randint(0, 9))

for i in range(len(start_list)):
    while i < len(start_list)/2 and number > len(start_list)/2:
        number = number - 1
        a = start_list[i] * start_list[number]
        end_list.append(a)
        i += 1

print("Начальный список:", start_list)
print("Конечный список:", end_list)