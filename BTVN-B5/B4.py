import random
n = int(input("Nhap so sinh vien: "))
khoa = ["CNTT", "KHMT", "KTPM", "HTTT", "DAPT"]
accounts ={}
for i in range(n):
    id = f"202360{str(i+1).zfill(4)}"
    password = random.choice(khoa) + id
    accounts[f"Account{i+1}"] = {
        "Username" : id,
        "Password" : password
    }
    
for id, detail in accounts.items():
    print(f"{id} : {detail}")
    
     