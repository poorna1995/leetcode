from typing import List

#Operation                        Time complexity 
# push value                   ---> O(1)
# pop value / remove value     ---> O(1)
# top value/ peek values       ---> O(1)
# get_max value                ---> O(1)


class MaxStack:
    
    def __init__(self):
        self.stack = []
        self. max_stack =[]
    
    def push(self, value:int):
        self.stack.append(value)
        value = self.stack[-1]
        if not self.max_stack or value >=self.max_stack[-1]:
            self.max_stack.append(value)
        return self.max_stack
    
    def pop(self):
        value = self.stack.pop()
        if value == self.max_stack[-1]:
            self.max_stack.pop()
        
        return self.max_stack, value
    
    def top(self):
        return self.stack[-1] if self.stack else None
    
    def get_max(self):
        return self.max_stack[-1] if self.max_stack else None
        
        

if __name__ == "__main__":
    maxstack = MaxStack()
    maxstack.push(5)
    maxstack.push(2)
    maxstack.push(8)
    maxstack.push(1)
    maxstack.push(3)
    
    print(maxstack.stack)
    print(maxstack.max_stack)
    print(maxstack.pop())
    print(maxstack.top())
    print(maxstack.get_max())