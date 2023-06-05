n = int(input())

def bisi(p):
  if(p%100==0):
    if(p%400==0):
      return "S"
    return "N"
  if(p%4==0):
    return "S"
  return "N"
while(n>0):
  p = int(input())
  print(bisi(p))
  n-=1
