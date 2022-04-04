# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:  
    def length(self, head):
        cnt = 0
        while head:
            head = head.next
            cnt += 1
        return cnt
        
    def helper(self, head, front_index, back_index, k):
                
        length = 0
        
        if head is None:
            return
        
        if front_index == k:
            self.first_head = head
            
        self.helper(head.next, front_index + 1, back_index - 1, k)
                
        if back_index == k:
            temp = self.first_head.val
            self.first_head.val = head.val
            head.val = temp
            return
            
    
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        self.first_head = None
        self.helper(head, 1, self.length(head), k)
        return head