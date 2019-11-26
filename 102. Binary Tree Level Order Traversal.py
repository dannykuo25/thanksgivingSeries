# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution():
    def levelOrder(self, root):
        if not root:
            return []
        ret = []
        level = [root]
        while level:
            curLevel = []
            nextLevel = []
            for node in level:
                curLevel.append(node.val)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            # ret.append([node.val for node in level])
            ret.append(curLevel)
            level = nextLevel
        return ret