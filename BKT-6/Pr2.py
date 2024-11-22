s = input("Nhap string: ")
my_val = {}
for char in s:
    if char != ' ':
        if (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z'):
            if char in my_val:
                my_val[char] += 1  
            else:
                my_val[char] = 1

# In kết quả
for key, value in my_val.items():
    print(f"{key} : {value}")
