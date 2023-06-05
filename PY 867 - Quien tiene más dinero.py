n = 5

lista = []
while(n>0):
  p = int(input())
  lista.append(p)
  n-=1

juan = lista[0]+lista[1]+lista[2]

pedro = lista[3]+lista[4]

if(pedro>juan):
  print("Pedro")
elif(juan>pedro):
  print("Juan")
else:
  print("")
