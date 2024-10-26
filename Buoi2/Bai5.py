a = int( input("a="))
#a
x = oct(a)[2:]
y = len(x)
print(y)
#b
c = dir(a)
print("Danh sach cac thuoc tinh cua va phuong thuc cua kieu du lieu number:")
for i in c:
    print(i)