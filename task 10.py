# # На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# # Определите минимальное число монеток, которые нужно перевернуть, 
# # чтобы все монетки были повернуты вверх одной и той же стороной. 
# # Выведите минимальное количество монет, которые нужно перевернуть.

# # Пример:

# # 5 -> 1 0 1 1 0
# # 2

# from random import randint
# days_num = int(input('Введите количество дней: '))
# warm_days, max_warm_days = 0, 0
# for _ in range(days_num):
#     temp = randint(-50, 50)
#     print(temp, end=' ')
#     if temp > 0:
#         warm_days += 1
#     else:
#         if warm_days > max_warm_days:
#             max_warm_days = warm_days
#         warm_days = 0
# print()
# if warm_days > max_warm_days:
#     max_warm_days = warm_days



from random import randint 

coin = int(input('Введите количество монет: '))
eagle = 0
tails = 0
for _ in range(coin):
    n = randint(0,1)
    print(n, end=' ')
    
    if n==0:
        tails+=1  
    else:
        eagle+=1
        
if eagle==0 or tails==0:
    print('Не нужно переворачисать') 
else:       
    if eagle<tails:
        print(f"Нужно перевернуть {eagle} раз")
    else:
        print(f"Нужно перевернуть {tails} раз")
