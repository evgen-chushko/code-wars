# Напишіть програму, яка отримує такі дані: 
# ім’я, вік, хобі, введені з клавіатури 
# (вводяться на окремих рядках), і
# друкує на екрані одним повідомленням повну
# інформацію на основі введених даних.

# Вхідні дані:

# Lord Voldemort
# 72
# Magic
# Вихідні дані:

# My name is Lord Voldemort. I am 72 and my hobby is Magic.

name=input("Input your name:")
age=int(input("Input your age:"))
hob=input("Input your hobby:")
print("My name is "+name+". I am",age,"and my hobby is "+hob)