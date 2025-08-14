from collections import defaultdict
from typing import Union


#Operation                        Time complexity 
# add value                    ---> O(1)
# get value / access value     ---> O(1)
# remove value / delete value  ---> O(1)



class Hashmap:
    def __init__(self):
        self.dicts = defaultdict(int)
    
    def put( self, key:Union[int,str], value:Union[int, str]) ->dict:
        self.dicts[key] = value
        return self.dicts
    
    def get(self, key:Union[int,str]) -> None:
        return self.dicts.get(key, -1)
    
    def remove(self, key:Union[int,str]) -> dict:
        if key in self.dicts:
            del self.dicts[key]
            return self.dicts
        else:
            return None
        
        




# class Hashmap:
    
#     def __init__(self):
#         self.dicts = defaultdict(int)
        
#     def put(self, key:Union[int,str], value:Union[int,str]) -> dict:
#         self.dicts[key] = value
#         return self.dicts
    
#     def get(self, key:Union[int,str]) -> Union[int,str]:
#         return self.dicts.get(key,-1)
    
#     def remove(self, key:Union[int, str]) -> dict :
#         if not self.dicts:
#             return None
#         else:
#             del self.dicts[key]
#             return self.dicts
    
    
    

if __name__ =="__main__":
    hashmap = Hashmap()
    hashmap.put("poorna",2)
    hashmap.put("chandana",5)
    hashmap.put("durgaharish",5)
    hashmap.put("chandran",5)
    
    print(hashmap.dicts)
    print(hashmap.get("jda"))
    print(hashmap.dicts)
    print(hashmap.remove("poorna"))
