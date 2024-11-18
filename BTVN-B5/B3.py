a = dict()
n = int(input("Nhập số cặp: "))
for _ in range(n):
    key = input("Nhập key: ")
    value = input("Nhập value: ")
    a[key] = value
    
seen = set()
swap_a = dict()
for key, value in a.items():
    if value in seen:
        print("None")
        break
    
    seen.add(value)
    swap_a[value] = key

else:
        print("Dict đã hoán đổi: ")
        for key,value in swap_a.items():
            print(f"{key} : {value}")
    