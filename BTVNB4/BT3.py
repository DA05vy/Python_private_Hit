n = int(input("Nhap n: "))
m = int(input("Nhap m: "))

num1 = [int(input(f"Nhap phan tu {_}: ")) for _ in range(n)]
num2 = [int(input(f"Nhap phan tu {_}: ")) for _ in range(m)]

list = [ x for x in num1 if x in num2]
print(list)