# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        prehead = ListNode(0)
        cur = prehead
        sum = 0
        while l1 or l2:
            # add l1
            if l1:
                sum += l1.val
                l1 = l1.next
            # add l2
            if l2:
                sum += l2.val
                l2 = l2.next

            cur.next = ListNode(sum % 10)
            cur = cur.next
            sum //= 10
        if sum != 0:
            cur.next = ListNode(sum % 10)
        return prehead.next