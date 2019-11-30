# recursively
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:    
#     # None  <-  1    <-    2    <- 3
#     #                              prev     cur      tmpNext
    def reverseList(self, head):
        if not head:
            return
        prev = None
        cur = head
        self.helper(cur, cur.next)
        return head
    
    def helper(self, prev, cur):
        if not cur:
            return
        self.helper(cur, cur.next)
        cur.next = prev
        


# iteratively
class Solution():
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        cur = head
        while cur != None:
            tmpNext = cur.next # save the next one
            cur.next = prev # change cur.next = prev
            prev = cur
            cur = tmpNext
        return prev
