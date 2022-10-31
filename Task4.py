# Задача №4: Задайте число N. Составьте список чисел Фибоначчи, N - количество чисел в списке


null_element = 0
first_element = 1
second_element = 1
n = int(input("Введите количество чисел Фибонначи: "))
if n==1:
    print(1)
elif n==2:
    print(1,1)
else:
    print (first_element, second_element, end=" ")
    for i in range (2, n):
        first_element, second_element = second_element, first_element + second_element 
        print(second_element, end = " ")

