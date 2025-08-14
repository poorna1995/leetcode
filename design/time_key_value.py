from collections import defaultdict

class TimeKeyValue:
    def __init__(self):
        self.dict = defaultdict(list)  
    
    def put(self, key: int, value: int, timestamp: int):
        self.dict[key].append((timestamp, value))
        
    def get(self, key: int, timestamp: int):
        if key not in self.dict:
            return ""  #
        
        arr = self.dict[key]
        l, r = 0, len(arr) - 1
        res = ""  
        
        while l <= r:
            mid = (l + r) // 2
            if arr[mid][0] <= timestamp:
                res = arr[mid][1]  
                l = mid + 1        
            else:
                r = mid - 1
        
        return res
