dki = set(input("Nhập tên các bạn đã đăng kí: ").split())
ckin = set(input("Nhập tên các bạn đã check-in: ").split())
not_ckin = set(item for item in dki if item not in ckin)
print("Những bạn chưa check-in: ", not_ckin )

tong = len(dki | ckin)
print("Tổng số lượng các bạn đã đăng ký và đã check-in:", tong)

print("Danh sách các bạn đã đăng ký theo thứ tự:", sorted(dki))



