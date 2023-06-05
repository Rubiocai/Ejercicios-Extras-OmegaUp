n = int(input())

while(n>0):
  p = list(map(int, input().split()))
  if(p[0]>p[1]):
    print(p[0])
  elif(p[0]<p[1]):
    print(p[1])
  else:
    print("NO ITZMAN")
  n-=1
