n = input()
n = n.split()
n[0] = int(n[0])
n[1] = int(n[1])

def expre(n):
  return (n[0]**3)+(n[1]**4) - 2*(n[0]**2)

if(expre(n)<680):
  print(n[0])
  print(n[1])

else:
  print("")
