lista = list(map(int, input().split()))

suma = sum(lista)
elem = 0

for i in lista:
  if(i!=0):
    elem += 1

print(suma, elem)
