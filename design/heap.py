class MinHeap:
    def __init__(self):
        self.heap = [0] # index 0 is not used, so that we can use 1-based index
    
    def push(self, val):
        self.heap.append(val)
        i = len(self.heap)-1

        
        #prelocate up
        while self.heap[i] < self.heap[i//2]:
            # temp = self.heap[i]
            # self.heap[i] = self.heap[i//2]
            # self.heap[i//2] = temp
            
            self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]
            i = i//2
        return self.heap
    
    
    def pop(self):
        if len(self.heap) <= 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()
        
        # frist pop the root value
        res = self.heap[1]
        
        # replace the laste to the root value
        
        last_val = self.head.pop()
        self.headp[1] = last_val
        i =1
        # check the heap proprty
        
        while 2*i< len(self.heap):
            if self.heap[2*i+1]<self.heap[2*i] and self.heap[i]>self.heap[2*i+1]:
                # swap with right child
                self.heap[i].self.heap[2*i+1]  = self.heap[2*i+1], self.heap[i]
                
                i = 2*i+1
            elif self.heap[2*i] < self.heap[i]:
                # swap with left child
                self.heap[i], self.heap[2*i] = self.heap[2*i], self.heap[i]
                i = 2*i
            else:
                break
        return res
    
    def heapify(self,arr):
        arr.append(arr[0])
        self.heap = arr
        curr = len(self.heap)-1 //2
        
        while curr >0:
            
            i =curr
            while 2*i < len(self.heap):
                if self.heap[2*i+1] < self.heap[2*i] and self.heap[i] > self.heap[2*i+1]:
                    # swap with right child
                    self.heap[i], self.heap[2*i+1] = self.heap[2*i+1], self.heap[i]
                    i = 2*i+1
                elif self.heap[2*i] < self.heap[i]:
                    # swap with left child
                    self.heap[i], self.heap[2*i] = self.heap[2*i], self.heap[i]
                    i = 2*i
                else:
                    break
        curr -=1
            

if __name__ == "__main__":
    min_heap = MinHeap()
    for i in range(1,10):
        min_heap.push(i)
        
    print(min_heap.heap)
            
        