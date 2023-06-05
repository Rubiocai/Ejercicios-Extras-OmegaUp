n = int(input())

while(n>0):
  pal = input()
  listilla = []
  for i in pal:
    listilla.append(i)
  cant = len(listilla)
  print('"' + pal + '"' + " tiene", cant, "caracteres")
  n-=1
