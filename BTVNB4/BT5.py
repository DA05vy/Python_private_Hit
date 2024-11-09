def binary( lst, x ):
    lst.sort()
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid = (left + right)//2
        if lst[mid] == x:
            return mid
        elif lst[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
        
    return -1

#1
lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x1 = 3
print(binary(lst1,x1))

#2 
lst2 = [10, 30, 50, 80, 99, 100, 140, 200]
x2 = 500
print(binary(lst2,x2))    