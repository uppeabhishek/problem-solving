from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        prev, cur, nxt = None, head, head.next

        while nxt:
            if cur.val == nxt.val:
                while nxt.next and nxt.val == nxt.next.val:
                    nxt = nxt.next
                if prev is None:
                    head = nxt.next
                else:
                    prev.next = nxt.next
                cur = nxt.next
                if cur:
                    nxt = cur.next
                else:
                    nxt = None
            else:
                prev = cur
                cur = nxt
                nxt = nxt.next

        return head


s = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(4)
head.next.next.next.next.next.next = ListNode(4)
head.next.next.next.next.next.next.next = ListNode(5)
head.next.next.next.next.next.next.next.next = ListNode(5)
head.next.next.next.next.next.next.next.next = ListNode(5)

# head = ListNode(1)
# head.next = ListNode(1)
# head.next.next = ListNode(1)
# head.next.next.next = ListNode(2)
# head.next.next.next.next = ListNode(3)
s.deleteDuplicates(head)
