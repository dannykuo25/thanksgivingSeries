class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        sum = 0
        d = {}
        d[0] = 1
        for i in range(len(nums)):
            sum += nums[i] # 20
            if sum - k in d: # 13
                cnt += d[sum - k]  
            if sum in d:
                d[sum] += 1
            else:
                d[sum] = 1 
        return cnt
    # [3,4,7,2,-3,1,4,2]
    #                 ^
    # d = {0:1, 3:1, 7:1, 14:2, 16:1, 13:1, 18:1, 20:1}
    # cnt = 4