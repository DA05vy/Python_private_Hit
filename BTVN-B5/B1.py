A = tuple(map(int, input("Nhập các số: ").split()))
B = tuple(input("Nhập các kí tự: ").split())

tong = sum(A)
avg = tong / len(A)
con = sum( 1 for i in range(len(A)) if A[i] > avg )
print(con)

even_A = tuple(x for x in range(len(A)) if x%2 == 0)
odd_A = tuple(x for x in range(len(A)) if x%2 != 0)
print("Tuple A chẵn: ", even_A)
print("Tuple A lẻ: ", odd_A)

k = input("Nhập kí tự k: ")
B_k = sum(1 for item in B if item == k)
print("Số kí tự giống k trong B: ", B_k)

B_x = [ item for item in B if len(item) >= 5 ]
print( "Các xâu kí tự có độ dài 5 trở lên: ", B_x)

C = tuple(zip(A, B))
print("Tuple C sau khi kết hợp A và B là:", C)




