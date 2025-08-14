class HashSet:
    def __init__(self):
        self.hashset = {}
    
    def put(self, key: int)->None: 
        if key not in self.hashset:
            self.hashset[key] = True
    
    def contain(self, key: int):
        return self.hashset[key] if key in self.hashset else False
    
    def remove(self,key:int):
        if key in self.hashset:
            del self.hashset[key]
        return self.hashset
        

if __name__ == "__main__":
    hash = HashSet()
    for i in range(1,20,3):
        hash.put(i)
    print(hash.hashset)
    print(hash.contain(4))
    print(hash.remove(10))
    
    
    
    
    
