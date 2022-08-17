# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None or head.next is None:
            return head
        
        
        odd_head, even_head = head, head.next
        
        odd, even = odd_head, even_head
        
        while odd and even:
            odd.next = even.next
            
            if not odd.next:
                break
            
            odd = odd.next
            
            even.next = odd.next
            even = even.next
        
        odd.next = even_head
        
        return odd_head