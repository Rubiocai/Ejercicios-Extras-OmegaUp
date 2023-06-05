n = int(input())
p = map(int, input().split())

cont = 0
for i in p:
  if(i==n):
    cont += 1

print(cont)
