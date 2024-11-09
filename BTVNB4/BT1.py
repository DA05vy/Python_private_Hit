k = int(input("Nhap so phan tu: "))
a = [int(input(f"Nhap phan tu {_}")) for _ in range(k)]
n = int(input("Nhap n: "))
m = int(input("Nhap m: "))
if n*m == k:
    matrix = [a[i:i + m] for i in range(0, n * m, m)]
    print("Ma tran X:")
    for row in matrix:
        print(row)
else:
    print("Khong the xay ma tran")
