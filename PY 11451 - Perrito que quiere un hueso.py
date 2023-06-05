a,b = map(int, input().split())
c,d = map(int, input().split())

if(a>c and b>d):
  print("Hueso 1")

elif(a<c and b<d):
  print("Hueso 2")

else:
  print("Perrito confundido :(")
