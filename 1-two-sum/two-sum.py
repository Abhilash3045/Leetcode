class Solution(object):
    def twoSum(self, nums, target):
        hm = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in hm:
                return (hm[comp], i)
            hm[num] = i
