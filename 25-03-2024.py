# 242
# a = int(input('Введите число А: '))
# b = int(input('Введите число B: '))
# if (a < b):
#  for i in range(a, b+1):
#    print(i, end=" ")
# else:
#  for i in range(a, b-1, -1):
#    print(i, end=" ")
# 243
# n = int(input("Введіть кількість чисел:")) 
# zeros = 0 
# for i in range(n):
#    num = int(input("Введіть число:"))
#    if num == 0:
#        zeros += 1  zero=zero + 1
# print(zeros)
# 244
# n = int(input())
# for i in range(10, 100):

# 245
# b = int(input())
# for i in range(1, b + 1, 2):
#     print(i, end=' ')
# 80
# number = input("Введіть п'ятицифрове число:")
# list(number)
# first_sum = int(number[0]) + int(number[2]) + int(number[4])
# second_sum = int(number[1]) + int(number[3])

# print(str(first_sum)+str(second_sum))

# 81
# n = int(input())
# print(n + 2 - n % 2)

# 146
# print('Введіть координати точки A (x1, y1): ')
# x1 = int(input())
# y1 = int(input())

# print('Введіть координати точки B (x2, y2): ')
# x2 = int(input())
# y2 = int(input())

# distance_a = (x1**2 + y1**2)**0.5
# distance_b = (x2**2 + y2**2)**0.5

# if distance_a > distance_b:
#     print('A')
# elif distance_b > distance_a:
#     print('B')
# else:
#     print('The distance is the same')

# 246 ((5 * 4) * 3) * 2
# n=int(input("Введіть число n:"))

# for i in range(n-1, 1, -1):
#     print(i)
#     n=n*i
# print(n)

def fact(n):
  n-=1
  if n==2:
    return n*(n-1)
  
  return fact(n)*(n-1)
print(fact(5))
