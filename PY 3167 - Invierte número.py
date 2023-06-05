n = int(input())

def inv_num(n):
    par_entera = 0
    num_inverso = 0
    while(n>0):
        par_entera = n%10
        num_inverso = (num_inverso*10)+par_entera
        n//=10
    return num_inverso

print(inv_num(n))
