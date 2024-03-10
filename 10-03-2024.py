# Напишіть програму, яка отримує три цілих числа, введені
# з клавіатури (кожне число вводиться на окремому рядку),
# і друкує на екрані їх суму, добуток,
# результат піднесення першого числа до степеня різниці
# другого і третього чисел.

# Вхідні дані:

# 2
# 3
# 6
# Вихідні дані:

# 11
# 36
# 0.125
# def num():
#   a=int(input("vvedite pervoye chislo:"))
#   b=int(input("vvedite vtoroye chislo:"))
#   c=int(input("vvedite tretiye chislo:"))

#   return a+b+c, a*b*c, a**(b-c)


# print(num())

# Напишіть програму, яка приймає ціле число n і обчислює
#  значення виразу n + nn + nnn.

# Вхідні дані:

# 5
# 3
# 1
# Вихідні дані:

# 615
# 369
# 123

# def n(a):
#   b = str(a)

#   result = a+int(b+b)+int(b+b+b)
  
#   return result

# print(n(5))

# A non-empty array a of length n is called an array of all possibilities if it contains all numbers between 0 and a.length - 1 (both inclusive).

# Write a function that accepts an integer array and returns true if the array is an array of all possibilities, else false.

# Examples:

# [1,2,0,3] => True
# # Includes all numbers between 0 and a.length - 1 (4 - 1 = 3)

# [0,1,2,2,3] => False
# # Doesn't include all numbers between 0 and a.length - 1 (5 - 1 = 4)

# [0] => True
# # Includes all numbers between 0 and a.length - 1 (1 - 1 = 0).

# def isAllPos(a):
#   if a[0]==0 and a.length<2:
#     return True