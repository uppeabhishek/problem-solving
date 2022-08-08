"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        new_head = None
        temp_new_head = None
        
        temp = head
        
        while temp:
                        
            temp_next = temp.next
            
            if not temp_new_head:
                temp_new_head = Node(temp.val)
                new_head = temp_new_head
            else:
                temp_new_head.next = Node(temp.val)
                temp_new_head = temp_new_head.next
            
            temp_new_head.random = temp
            temp.next = temp_new_head
            
            temp = temp_next
            
        
        temp = new_head
                
        while temp:
            if temp.random.random:
                temp.random = temp.random.random.next
            else:
                temp.random = None
            temp = temp.next
        
        
        
        return new_head
            
        