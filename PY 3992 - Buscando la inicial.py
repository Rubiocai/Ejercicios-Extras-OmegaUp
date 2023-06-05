letrafav = input()
palabras = int(input())

lista = []
while(palabras>0):
  pal = input()
  lista.append(pal)
  palabras-=1

for i in lista:
  if(i[0]==letrafav):
    print(i)
