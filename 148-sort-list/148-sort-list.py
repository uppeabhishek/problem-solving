# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge2Lists(self, l1, l2):
        if l1 is None:
            return l2

        if l2 is None:
            return l1

        if l1.val <= l2.val:
            l1.next = self.merge2Lists(l1.next, l2)
            return l1

        l2.next = self.merge2Lists(l1, l2.next)
        return l2

    def splitList(self, head):
        if head.next is None:
            return head, None

        slow = head
        fast = head.next
        prev = head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        if fast:
            prev = slow
            second = slow.next
        else:
            second = slow
        
        prev.next = None

        return head, second

    def mergeSort(self, head):
        first, second = self.splitList(head)

        if second is None:
            return first

        head1 = self.mergeSort(first)
        head2 = self.mergeSort(second)
        result = self.merge2Lists(head1, head2)
        return result

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        return self.mergeSort(head)