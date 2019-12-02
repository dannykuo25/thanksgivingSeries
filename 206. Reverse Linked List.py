# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# recursively
# time: O(n), space: O(n)
class Solution:
    def reverseList(self, head):
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
# time: O(n), space: O(1)
class Solution2:
    def reverseList(self, head):
        prev = None
        cur = head
        while cur != None:
            tmpNext = cur.next # save the next one
            cur.next = prev # change cur.next = prev
            prev = cur
            cur = tmpNext
        return prev