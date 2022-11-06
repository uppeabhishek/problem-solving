# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from python.leetcode.SortLinkedList import ListNode


class Solution:

    def reverse(self, head, cnt, k, next_pointer):

        if head is None or head.next is None or cnt == k:
            return head

        temp = self.reverse(head.next, cnt + 1, k, next_pointer)

        if next_pointer[0] is None:
            next_pointer[0] = head.next.next

        head.next.next = head
        head.next = None

        return temp

    def length(self, head):
        slow, fast = head, head
        cnt = 0

        while fast and fast.next:
            slow = slow.next
            fast = fast.next
            cnt += 2

        return cnt + 1 if fast else cnt

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        current_head = head
        next_pointer = [None]

        def helper(current_head):
            if current_head is None:
                return

            next_pointer = [None]

            first = self.reverse(current_head, 1, k, next_pointer)
            helper(next_pointer[0])

            print (first, current_head)

        helper(current_head)


s = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)

s.reverseKGroup(head, 2)
