class MyStack:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.ds = []
    def isEmpty(self):
        if len(self.ds) == 0:
            return True
        else:
            return False
    def isFull(self):
        if len(self.ds) == self.capacity:
            return True
        else:
            return False
    def Pop(self):
        if (len(self.ds) != 0):
            return self.ds.pop()
    def Push(self,val):
        if len(self.ds) != self.capacity:
            self.ds.append(val)
        else: 
            #print(f"Danh sach full, khong the them")
            return False
    def Top(self):
        if len(self.ds) != 0:
            return self.ds[len(self.ds)-1]
        else:
            #print(f"Danh sach trong")
            return False

stack1 = MyStack(capacity=5)
stack1.Push(1)
stack1.Push(2)
print(stack1.isFull())

print(stack1.Top())

print(stack1.Pop())

print(stack1.Top())

print(stack1.Pop())

print(stack1.isEmpty())
