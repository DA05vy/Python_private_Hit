class MyStack:
    def __init__ (self,capacity: int):
        self.capacity = capacity
        self.list = []
    #kiem tra stack rong khong
    def isEmpty(self: bool):
        if len(self.list) == 0:
            return True
        else:
            return False
    #kiem tra stack full chua
    def isFull(self: bool):
        if len(self.list) == self.capacity:
            return True
        else:
            return False
    #loai bo top element va tra ve gia tri do
    def pop(self: int):
        if len(self.list) != 0:
            return self.list.pop()
        else:
            pass
    #lay gia tri top hien tai cua stack
    def top(self: int):
        if len(self.list) != 0:
            return self.list[len(self.list)-1]
        else:
            pass
    #them gia tri value vao stack
    def push(self, value):
        if len(self.list) != self.capacity:
            self.list.append(value)
        else:
            pass
    
    
stack1 = MyStack(capacity=5)
stack1.push(1)
stack1.push(2)

print(stack1.isFull())
# >> False
print(stack1.top())
# >> 2
print(stack1.pop())
# >> 2
print(stack1.top())
# >> 1
print(stack1.pop())
# >> 1
print(stack1.isEmpty())
# >> True
print()

stack2 = MyStack(capacity=4)
stack2.push(31)
stack2.push(12)
stack2.push(10)
stack2.push(20)
print(stack2.isFull())
# >> True
print(stack2.top())
# >> 20
print(stack2.pop())
# >> 20
print(stack2.top())
# >> 10
print(stack2.pop())
# >> 10
print(stack2.isEmpty())
# >> False
