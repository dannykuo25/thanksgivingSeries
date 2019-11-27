class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# time: O(n), space: O(L), where L means the largest number of nodes in a single layer of binary tree
# L = (n + 1)/2 -> O(n)
class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        level = [root]
        ret = []
        flag = -1 # -1 means reverse
        while level:
            # add result
            curLevel = []
            for node in level:
                curLevel.append(node.val)
            ret.append(curLevel) # [[3], [20, 9], [1,2,15,7]]
            nxtLevel = []
            for node in reversed(level): # 9, 20
                if flag == 1:
                    if node.left:
                        nxtLevel.append(node.left) # 1
                    if node.right:
                        nxtLevel.append(node.right) # 2  
                else:
                    if node.right:
                        nxtLevel.append(node.right) # 15
                    if node.left:
                        nxtLevel.append(node.left) # 7
            flag *= -1
            level = nxtLevel
        return ret

#         3
#     9      20
# 1     2  15   7