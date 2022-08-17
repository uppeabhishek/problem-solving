# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def length():
            slow, fast, cnt = head, head, 0
            
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                cnt += 2
            
            if fast:
                cnt += 1
            
            return cnt
    
        def helper():
            
            if head is None or head.next is None:
                return head
            
            nonlocal k
            
            le = length()
            
            k = k % le
            
            if k == 0:
                return head
            
            temp = head
        
            i = 1
            
            while i < le - k:
                temp = temp.next
                i += 1
            
            new_head = temp.next
            temp.next = None
            
            temp = new_head
            
            while temp.next:
                temp = temp.next
            
            temp.next = head
            
            return new_head
            
            
        return helper()