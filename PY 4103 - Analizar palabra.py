pal = input()

cont = 0
voc = 0
palinv = ""
paaux = []

for i in pal:
  cont += 1
  if(i=='a'or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
    voc += 1

for i in pal:
  paaux.insert(0,i)

for j in paaux:
  palinv += j

print(cont)
print(voc)
print(palinv)
