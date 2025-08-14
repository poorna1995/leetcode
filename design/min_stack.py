from typing import List

#Operation                        Time complexity 
# push value                   ---> O(1)
# pop value / remove value     ---> O(1)
# top value/ peek values       ---> O(1)
# get_min value                ---> O(1)


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self, value:int) -> None:
        self.stack.append(value)
        if not self.min_stack or value<= self.min_stack[-1]:
            self.min_stack.append(value)
        return self.min_stack 
    
    def remove(self):
        if not self.stack:
            return []
        value = self.stack.pop()
        print(f"Popped value: {value}")
        if value  == self.min_stack[-1]:
            self.min_stack.pop()
        return self.min_stack, value
    
    
    def top(self):
        if not self.stack:
            return None
        return self.stack[-1]
    
    def get_min(self):
        return self.min_stack[-1] if self.min_stack else None
    

    
    
if __name__ == "__main__":
    minstack = MinStack()
    
    minstack.push(5)
    minstack.push(2)
    minstack.push(8)
    minstack.push(1)
    minstack.push(3)
    
    

        
    print(minstack.stack)
    print(minstack.min_stack)
    print(minstack.remove())
    print(minstack.top())
    print(minstack.get_min())
    

    

        


