# Задача №2: Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

numbers_list = [1.1, 1.2, 3.1, 10.01]
max = 0
min = 1
for i in numbers_list:
    if max <= (i - int(i)):
        max = i - int(i)
    if min >= i - int(i):
        min = i - int(i)
difference = (max - int(max)) - (min - int(min))

print("Начальный список:", numbers_list)
print(f"Максимальное значение {round(max, 2)} и минимальное значение {round(min, 2)}" )
print("Разница между максимальным значением и минимальным: ", round(difference, 2))
  