# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        def reverse(head):
            
            if head is None or head.next is None:
                return head
            
            temp = reverse(head.next)
            
            head.next.next = head
            head.next = None
            
            return temp
            
            
        def helper():
            
            if head is None or head.next is None:
                return head
            
            prev = None
            slow, fast = head, head
            
            while fast and fast.next:
                prev = slow
                slow = slow.next 
                fast = fast.next.next
            
            prev.next = None

            first = head
            second = slow
            
            prev_second = None
            second = reverse(second)
            
            while first:
                prev_second = second
                temp1, temp2 = first.next, second.next
                
                first.next = second
                second.next = temp1
                
                first = temp1
                second = temp2
                
                if not first:
                    prev_second.next = second
            
        helper()
        return 