# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        diameter = [0]
        self.depth(root, diameter)
        return diameter[0]

    def depth(self, root, diameter):
        if not root: 
            return 0
        leftDepth = self.depth(root.left, diameter)
        rightDepth = self.depth(root.right, diameter)
        diameter[0] = max(diameter[0], leftDepth + rightDepth)
        return 1 + max(leftDepth, rightDepth)

#     1
#    /  \
#   2    3
#  / \ 
# 4   5
