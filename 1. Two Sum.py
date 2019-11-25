# two iterations
# hashmap
# time: O(N), space: O(N)
class Solution:
    def twoSum(self, nums, target):
        n = len(nums)
        dic = {}      
        for i in range(n):
            dic[nums[i]] = i
        for i in range(n):
            if target - nums[i] in dic and dic[target - nums[i]] != i:
                return [i, dic[target - nums[i]]]
                
# one iteration
class Solution2:
    def twoSum(self, nums, target):
        n = len(nums)
        dic = {}      
        for i in range(n):
            if target - nums[i] not in dic:
                dic[nums[i]] = i
            else:    
                return [i, dic[target - nums[i]]]

print(Solution2().twoSum([3,3], 6))