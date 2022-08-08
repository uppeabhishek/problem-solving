"""
# Definition for a Node.
"""


class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):

        new_head = None
        temp_new_head = None

        temp = head

        while temp:

            temp_next = temp.next

            if not temp_new_head:
                temp_new_head = Node(temp.val)
                new_head = temp_new_head
            else:
                temp_new_head.next = Node(temp.val)
                temp_new_head = temp_new_head.next

            temp_new_head.random = temp
            temp.next = temp_new_head

            temp = temp_next

        temp = new_head

        while temp:
            if temp.random.random:
                temp.random = temp.random.random.next
            else:
                temp.random = None

            temp = temp.next


s = Solution()
h1 = Node(7)
h1.next = Node(13)
h1.next.next = Node(11)
h1.next.next.next = Node(10)
h1.next.next.next.next = Node(1)

h1.random = None
h1.next.random = h1
h1.next.next.random = h1.next.next.next.next
h1.next.next.next.random = h1.next.next
h1.next.next.next.next.random = h1

s.copyRandomList(h1)