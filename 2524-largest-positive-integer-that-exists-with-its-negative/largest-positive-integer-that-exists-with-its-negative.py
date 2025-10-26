class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        r=0
        i=len(nums)-1
        while i>0:
            if -(nums[i]) in nums:
                return nums[i]
            i-=1
        return -1