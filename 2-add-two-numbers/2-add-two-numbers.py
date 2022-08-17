# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        head1, head2 = l1, l2
        
        rem = 0
        
        head = None
        temp = None
        
        while head1 and head2:
            current = head1.val + head2.val + rem
            
            if current  > 9:
                rem = current // 10
                current = current % 10
            else:
                rem = 0
            
            if head is None:
                head = ListNode(current)
                temp = head
            else:
                temp.next = ListNode(current)
                temp = temp.next
        
            head1, head2 = head1.next, head2.next
            
        
        while head1:
            current = head1.val + rem
            
            if current > 9:
                rem = current // 10
                current = current % 10
            else:
                rem = 0
            
            temp.next = ListNode(current)
            temp = temp.next
            head1 = head1.next
            
        
        while head2:
            current = head2.val + rem
            
            if current > 9:
                rem = current // 10
                current = current % 10
            else:
                rem = 0
            
            temp.next = ListNode(current)
            temp = temp.next
            head2 = head2.next
            
        
        if rem:
            temp.next = ListNode(rem)
        
        return head

    
    
    
    
                