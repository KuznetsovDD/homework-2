# Требуется вывести все целые степени двойки 
# (т.е. числа вида 2**k), не превосходящие числа N.

# Пример:

# 10 -> 1 2 4 8



numb = int(input("Введите натуральное число: "))

power = 0
i=0
while power <= numb:
    power = 2**i
    if power <= numb:
        print(power, end=" ")
        i+=1
    