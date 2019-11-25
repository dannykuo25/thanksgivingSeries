# two iterations
# hashmap
# time: O(N), space: O(N)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        dic = {}      
        for i in range(n):
            dic[nums[i]] = i
        for i in range(n):
            if target - nums[i] in dic and dic[target - nums[i]] != i:
                return [i, dic[target - nums[i]]]
                
# one iteration
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        dic = {}      
        for i in range(n):
            dic[nums[i]] = i
        for i in range(n):
            if target - nums[i] in dic and dic[target - nums[i]] != i:
                return [i, dic[target - nums[i]]]
