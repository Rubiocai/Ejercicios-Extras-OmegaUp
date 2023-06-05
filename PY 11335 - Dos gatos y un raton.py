a,b,c = map(int, input().split())

gat1 = c-a
gat2 = c-b

if(gat1<0):
  gat1 = gat1 * -1

if(gat2<0):
  gat2 = gat2 * -1

if(gat1==gat2):
  print("raton C")

elif(gat1<gat2):
  print("gato A")

else:
  print("gato B")
