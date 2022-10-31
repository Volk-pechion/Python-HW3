# Задача №3: Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number = int(input("Введите 10-тичное число: "))
numbers_list = []
count = 0
while number>0:
    count = number%2
    numbers_list.append(count)
    number = number//2
print(number)
print(numbers_list)
numbers_list.reverse()
print(numbers_list)
print("В двоичной системе число выглядит:","".join(map(str, numbers_list)))