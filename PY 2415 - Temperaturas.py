t = int(input())

if(t<0):
  print("Muy Frio")
elif(t==0 or t<=10):
  print("Frio")
elif(t==11 or t<=20):
  print("Templado")
elif(t==21 or t<=25):
  print("Calido")
else:
  print("Muy Calido")
