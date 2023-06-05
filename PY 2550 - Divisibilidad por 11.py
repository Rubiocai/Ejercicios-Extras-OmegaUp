n = int(input())

while(n>0):
  num = int(input())
  if(num%11==0):
    print("El número", num,"es divisible por 11")
    n-=1
  else:
    print("El número", num,"no es divisible por 11")
    n-=1
