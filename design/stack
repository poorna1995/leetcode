class MyStack:
    def __init__(self):
        self.q1 = deque() # main deck
        self.q2 = deque() # stack immplenetm

    def push(self, x: int) -> None:  # O(1)
        self.q1.append(x)

    def pop(self) -> int:  # O(n)
        if not self.q1:
            return None
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
            top = self.q1.popleft()
            self.q1, self.q2 = self.q2, self.q1
        return top
    def top(self) -> int:  # O(n)
        if not self.q1:
            return None
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
            top = self.q1.popleft()
            self.q2.append(top)
            self.q1, self.q2 = self.q2, self.q1
        return top

    def empty(self) -> bool:  # O(1)
        return not self.q1
    
    
    

if __name__ = "__main__":
    stack = MyStack()
    for i in range(10):
        stack.push(i)
    print(stack.q1)