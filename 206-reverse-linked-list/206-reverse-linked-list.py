# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def reverseListHelper(self, head):
        if head is None or head.next is None:
            return head
        
        temp = self.reverseListHelper(head.next)  
        
        head.next.next = head
        head.next = None
        
        return temp  
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverseListHelper(head)