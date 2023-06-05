n,a,b = map(int, input().split())

while(n<1000):
  if(n%2==0):
    for i in range(1,a+1):
      n += i
  else:
    for j in range(1,b+1):
      n += j

print(n)
