# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if self.isMatch(s, t):
            return True
        if not s:
            return False
        
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    
    def isMatch(self, s, t):
        if (not s and t) or (not t and s):
            return False
        if not s and not t:
            return True
        if s.val == t.val:
            return self.isMatch(s.left, t.left) and self.isMatch(s.right, t.right)
        else:
            return False
    