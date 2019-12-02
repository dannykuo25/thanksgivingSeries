# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# recursively
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        cur = head
        return self.helper(prev, cur)
    
    def helper(self, prev, cur):
        if cur == None:
            return prev
        end = self.helper(cur, cur.next)
        cur.next = prev
        return end
        
        
# iteratively
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        cur = head
        while cur != None:
            tmpNext = cur.next # save the next one
            cur.next = prev # change cur.next = prev
            prev = cur
            cur = tmpNext
        return prev