


# edges, values 
# dict ( str, [str2, str3, ...] )
# use defalut dict

from collections import defaultdict
from typing import Set
from collections import deque

class Graph:
    
    def __init__(self):
        self.adj = defaultdict[int, Set[int]] = defaultdict(set) # {"delhi":["mumbai", "chennai"], "mumbai":["delhi", "chennai"]}
    
    def add_edge(self, src:int, dest:int):
        if src in self.adj and dest in self.adj[src]:
            return
        else:
            self.adj[src].add(dest)
            
            
    def removeEdge(self, src, dest):
        if src in self.adj and dest in self.adj[src]:
            self.adj[src].remove(dest)
            return True
        return False
    
    def hasPath(src, dest):
        if src == dest:
            return True
        if src not in self.adj:
            return False
        
        
        q = deque([src])
        visited = set()
        visited.add(src)
        
        while q:
            v = q.popleft()
            for u in self.adj.get(v,()):
                if u ==dest:
                    return True
                if u not in visited:
                    visited.add(u)
                    q.append(u)
                    
        return False            
        
        
        
        
    