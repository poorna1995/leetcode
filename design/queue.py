class MyQueue:
    def __init__(self):
        self.stack_in = []   # main stack
        self.stack_out = []  # queue
    
    def enqueue(self, x: int) -> None:
        self.stack_in.append(x)
    
    def dequeue(self) -> int:
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        if not self.stack_out:  # queue is empty
            return None
        return self.stack_out.pop()
    
    def peek(self) -> int:
        # Move if needed
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out[-1] if self.stack_out else None
    
    def empty(self) -> bool:
        return not self.stack_in and not self.stack_out


# Example usage
if __name__ == "__main__":
    q = MyQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue())  
    print(q.peek())     
    print(q.empty())    
