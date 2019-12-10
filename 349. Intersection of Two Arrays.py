# time: O(n + m)
# space: O(min(n, m))
class Solution2():
    def intersection(self, nums1, nums2):
        if len(nums1) > len(nums2):
            return self.intersection(nums2, nums1)
        res = []
        count = set()
        # put nums1 into count
        for num in nums1:
            if num not in count:
                count.add(num)
        
        # check if nums2 
        for num in nums2:
            if num in count:
                res.append(num)
                count.remove(num)
        return res

# trying two sets
class Solution():
    def intersection(self, nums1, nums2):
        res = []
        count1 = set(nums1)
        count2 = set(nums2)

        for num in count1:
            if num in count2:
                res.append(num)
                count2.remove(num)

        return res