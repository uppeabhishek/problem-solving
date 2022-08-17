# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        if head.next is None:
            return True
        
        def reverse(head):
            if head is None or head.next is None:
                return head
                        
            temp = reverse(head.next)                  
            head.next.next = head
            head.next = None
            
            return temp
            
        def helper():
            prev = None
            slow, fast = head, head
            
            while fast and fast.next:
                prev = slow
                slow = slow.next 
                fast = fast.next.next
            
            prev.next = None

            if fast:
                second = slow.next
                prev.next = None
            else:
                second = slow
            
            first = reverse(head)
            
            
            while first and second:
                if first.val != second.val:
                    return False
                first = first.next
                second = second.next
            
            return True
        
        return helper()
        
                
            
            
            