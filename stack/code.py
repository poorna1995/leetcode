class Stack:
    def __init__(self):
        self.stack =[]
    def push(self, num):
        self.stack.append(num)
    def pop(self):
        self.stack.pop()
    def peek(self):
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack)==0
    
    def size(self):
        return len(self.stack)
        
    def clear(self):
        self.stack =[]
        
    def contain(self,element):
        return element in self.stack
        


output = Stack()

output.push(1)
output.push(2)
output.push(3)
output.push(4)

print(output.stack)

print(output.size())
output.pop()
print(output.stack)

print(output.contain(5))

