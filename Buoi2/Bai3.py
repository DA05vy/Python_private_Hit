s1 = "Chao mung den CLB Tin Hoc HIT"
print(s1)
s2 = "CLB Tin Hoc HIT truc thuoc Khoa CNTT  - “10 diem”"
print(s2)

s3 = "CLB Tin Hoc HIT truc thuoc Khoa CNTT"
for i in s3:
    if i.isupper():
        print(i, end= ' ')
print()
for i in s3:
    if i.islower():
        print(i, end= ' ')

s4 = "CLB Tin Hoc HIT truc thuoc Khoa CNTT"
if ( "CNTT" in s4 ):
    print("Yes")
else:
    print("No")

s5 = "CLB Tin Hoc HIT truc thuoc Khoa CNTT"
s6 = s5.swapcase()
print(s6)

