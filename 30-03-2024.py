def fact(m):
  for i in range(m-1, 1, -1):
    m=m*i
  return m    

n=int(input("Введіть ціло число:"))
sum=0
for i in range(1, n+1):
  
  print(fact(i))

