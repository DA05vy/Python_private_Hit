a = int( input("a="))
b = int( input("b="))
print ("a + b=", a+b)
print ("a - b=", a-b)
print ("a * b=", a*b)
print ("a // b=", a//b)
print ("a ** b=", a**b)
print ("a % b=", a%b)

if a > b:
    print( "a>b" )
elif a == b:
    print( "a=b" )
else:
    print( "a<b" )

print ("a and b:", a and b)
print ("a or b:", a or b)
print ("a xor b", a ^ b)
print ("NOT a==b", ~ a==b)
print ("a>>5=", a>>5)
print ("a<<5=", a<<5)
x = bin(a)[2:]
print ("He co so 2 cua a:", x)
y = x[::-1]
print ("He co 2 dao nguoc cua a:", y)
