# time: O(nlog(n) + mlog(m))
# space: O(1)
class Solution2:
    def intersect(self, nums1, nums2):
        if not nums1 or not nums2:
            return []
        res = []
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        while i != len(nums1) and j != len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                res.append(nums1[i])
                i += 1
                j += 1
        return res

# time: O(n + m)
# space: O(min(n, m))
class Solution:
    def intersect(self, nums1, nums2):
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)
        res = []
        # put nums1 into count dic
        count = {}
        for num in nums1:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        # every nums2, check count contain num
        for num in nums2:
            if num in count and count[num] > 0:
                res.append(num)
                count[num] -= 1
        return res


nums1 = [4,9,5] 
nums2 = [9,4,9,8,4]
print(Solution().intersect(nums1, nums2))