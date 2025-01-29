class Queue:
    def __init__(self):
        self.queue =[]
    
    def add(self, num):
        self.queue.append(num)
        
    def dequeue(self):
        if len(self.queue)>0:
            return self.queue.pop(0)
        else:
            return "Queue is empty"
    def isEmpty(self):
        if len(self.queue) ==0:
            return "empty"
        
    

q = Queue()
q.add(1)
q.add(2)
q.add(3)
q.add(4)
print(q.queue)
q.dequeue()
print(q.queue)
