N = int(input())
for i in range(N):
  x = int(input())
  cont = 0
  for j in range(1, x+1):
    if x % j == 0:
      cont+= 1
  if cont > 2:
    print("%d nao eh primo" %x)
  else:
    print("%d eh primo" %x)  
  