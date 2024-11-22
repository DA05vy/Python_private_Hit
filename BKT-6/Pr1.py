n = 10000
def d (x):
    if ( x == 0 or x == 1 ):
        return 1 
    return x*d(x-1)

x = int(input("Nhap x: "))
e = 1
for i in range(1,n+1):
    e = e + (x**i)/d(i)
    
print( f"e^x = {e} ")