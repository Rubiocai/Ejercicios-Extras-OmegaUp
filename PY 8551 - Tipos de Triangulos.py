n = input()
n = n.split()
n[0] = int(n[0])
n[1] = int(n[1])
n[2] = int(n[2])

if(n[0]==n[1] and n[0]==n[2] and n[1]==n[2]):
  print("equilatero")
elif(n[0]==n[1] or n[0]==n[2] or n[1]==n[2]):
  print("isosceles")
else:
  print("escaleno")
