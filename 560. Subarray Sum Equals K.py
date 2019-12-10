# Input:nums = [1,1,1], k = 2
# Output: 2

# **Complexity Analysis**
# Time complexity : O(n^2). We need to consider every subarray possible.
# Space complexity : O(1). Constant space is used.
# result: TLE
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        for i in range(0, len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                if sum == k:
                    cnt += 1
        return cnt

