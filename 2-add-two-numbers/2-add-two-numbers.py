# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addToResult(self, res, val):
        if res is None:
            res = ListNode(val)
            self.result = res
        else:
            res.next = ListNode(val)
            res = res.next
        return res
        
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rem = 0
        
        res = None
        
        self.result = None
        
        while l1 and l2:
            su = l1.val + l2.val + rem
            if su >= 10:
                res = self.addToResult(res, su % 10)
                rem = su // 10
            else:
                res = self.addToResult(res, su)
                rem = 0
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            su = l1.val + rem
            if su >= 10:
                res = self.addToResult(res, su % 10)
                rem = su // 10
            else:
                res = self.addToResult(res, su)
                rem = 0
            l1 = l1.next
        
        while l2:
            su = l2.val + rem
            if su >= 10:
                res = self.addToResult(res, su % 10)
                rem = su // 10
            else:
                res = self.addToResult(res, su)
                rem = 0
            l2 = l2.next
        
        if rem > 0:
            self.addToResult(res, rem)
        
        return self.result

        