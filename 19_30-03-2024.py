# 57
# m=float(input("Write m of apple pie:"))
# 
# flour=m*0.28
# print("flour weight:", float(dough)-float(eggsSugar))


# 58
# a=int(input())
# b=int(input())
# print(a//b,a%b)


# 143
# num=int(input("Введіть номер від 0 до 36: "))
# if num < 0 or num > 36:
#   print("Номер повинен бути в діапазоні від 0 до 36")
# elif num == 0:
#   print("Зелений")
# elif (1 <= num <= 10) or (19 <= num <= 28):
#   if num %2==1:
#     print("Red") 
#   print("Black") 
# elif (11 <= num <= 18) or (29 <= num <= 36):    
#     if num % 2 == 1:
#         print("Black")
#     print("Red")

# Вхідні дані:

# 6
# 3
# Вихідні дані:

# 0 	0 	0
# 1 	1 	1
# 2 	2 	2
# 3 	3 	3
# 4 	4 	4
# 5 	5 	5
# 6 	6 	6









# 241
# n = int(input("Введіть значення n: "))
# for i in range(1, n + 1):
#         for k in range(i, n + 1):
#             print(k, " ", end="")
#         print()
# 240
# n = int(input("Введіть значення n: "))
# m = int(input("Введіть значення m: "))
# for i in range(n + 1):
#     for j in range(m):
#         print(i, " ", end="")
#     print()
# # 144
# workingHours = int(input())
# selary = int(input())
# increasedSelary = selary * 1.5
# if workingHours > 40:
#     print(40*selary + (workingHours - 40) * increasedSelary)
# else:
#     print(workingHours*selary)
# 79
a = int(input("Введіть кількість учнів у класі A: "))
b = int(input("Введіть кількість учнів у класі B: "))
c = int(input("Введіть кількість учнів у класі C: "))
total = a + b + c
if total % 2 == 0:
    print(total // 2)
else:
    print((total + 1) // 2)





