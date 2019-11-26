"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        ret = root
        while root != None and root.left != None:
            cur = root
            while cur != None:
                cur.left.next = cur.right
                cur.right.next = None if cur.next == None else cur.next.left
                cur = cur.next
            root = root.left
        return ret

# java solution
# class Solution {
#     public Node connect(Node root) {
#         Node ret = root;
#         while(root != null && root.left != null) {
#             Node cur = root;
#             while(cur != null) {
#                 cur.left.next = cur.right;
#                 cur.right.next = cur.next == null ? null : cur.next.left;
#                 cur = cur.next;
#             }
#             root = root.left;
#         }
#         return ret;
#     }
# }