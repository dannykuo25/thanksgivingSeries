# brute force 
# time: O(n^2), space: O(1)
class Solution:
    def trap(self, height: List[int]) -> int:
        ret = 0
        for i in range(len(height)):
            maxL, maxR = 0, 0
            for j in reversed(range(0, i)):
                maxL = max(maxL, height[j])
            for j in range(i + 1, len(height)):
                maxR = max(maxR, height[j])
            if min(maxL, maxR) - height[i] > 0:
                ret += min(maxL, maxR) - height[i]
        return ret

class Solution2:
    def trap(self, height):
        if not height:
            return 0
        n = len(height)
        ret = 0
        leftMax = [0] * n
        rightMax = [0] * n
        leftMax[0] = height[0]
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])
        rightMax[n - 1] = height[n - 1]
        for i in reversed(range(0, n - 1)):
            rightMax[i] = max(rightMax[i + 1], height[i])
        for i in range(0, n):
            if min(leftMax[i], rightMax[i]) - height[i] > 0:
                ret += min(leftMax[i], rightMax[i]) - height[i]
        return ret