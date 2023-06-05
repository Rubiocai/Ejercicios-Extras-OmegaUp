n = int(input())

contador = 1
while(n>1):
  if(n%2==0):
    n = n/2
    contador+=1
  else:
    n = (n*3)+1
    contador+=1
  
print(contador)
