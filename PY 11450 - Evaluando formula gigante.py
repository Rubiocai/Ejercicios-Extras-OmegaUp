x,y,z = map(float, input().split())

ecua = (((2*x+y)/z)*((y*y*y)-z))/(((x+(2*y)+(3*z))/(z-(2*y)-(3*x)))+(x*x)+(z*z))

print(ecua)
