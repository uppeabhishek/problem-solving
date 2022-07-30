# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    
    def reverseLinkedList(self, head):
        prev, cur, nxt = None, head, head
        
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
                
        return prev
        
    def reverseSecondPart(self, head):
        slow, fast = head, head
        prev_slow = None
        
        while fast:
            prev_slow = slow
            slow = slow.next
            fast = fast.next.next
        
        prev_slow.next = None
        
        first = head
        second = self.reverseLinkedList(slow)
        
        
        return (first, second)
            
        
    def pairSum(self, head: Optional[ListNode]) -> int:
        first, second = self.reverseSecondPart(head)
        
        max_val = 0
        
        
        while first:
            max_val = max(max_val, first.val + second.val)
            first = first.next
            second = second.next
        
        return max_val