def merge(a,b):
    res = []
    i,j = 0, 0
    while i < len(a) and j < len(b):
        res.append(a[i])
        i += 1
        res.append(b[j])
        j += 1
        
    while i < len(a):
        res.append(a[i])
        i += 1
        
    while j < len(b):
        res.append(b[j])
        j += 1
    
    return res

#1
a = [1,2,3,4,5]
b = [6,7,8]
print(merge(a,b))

#2
c = [1,2,3]
d = [6,7,8,9,10]
print(merge(c,d))

#3 
e = [1,2,3,4]
f = [6,7,8,9]
print(merge(e,f))

#5
g = ['a', 'b', 'c']
h = [10,11,12]
print(merge(g,h))