class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def travasal(self):
        curr_head = self.head
        
        while curr_head:
            curr_head = currcurren_head.next
        
    def search(self, key):
        curr_head = self.head
        while curr_head:
            if key == curr_head.val:
                return True
            curr_head = curr_head_next
        return False
    
    def insert(self, val):
        new_node = ListNode(val, None)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    def delete(self, val):
        if self.head is None:
            return None

        if self.head.val == val:
            self.head = self.head.next
            return
            
            current_head = self.head
            while current_head.next:
                if current_head.next.val == val:
                    current_head.next = current_head.next.next
                    return
                current_head = current_head.next
            
        
    








if __name__ = "__main__":
    # Example usage
    ll = LinkedList(None)
    ll.addAtHead(1)
    ll.addAtHead(2)
    print(ll.head.val)  
    print(ll.head.next.val)  
                