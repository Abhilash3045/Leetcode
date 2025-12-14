class Solution:
    def splitArray(self, nums: List[int]) -> int:
        maxy=nums.index(max(nums))
        for i in range(maxy):
            if nums[i]>=nums[i+1]:
                return -1
        for i in range(maxy+1,len(nums)-1):
            if nums[i]<=nums[i+1]:
                return -1
        if maxy<len(nums)-1 and nums[maxy]==nums[maxy+1]:
            return abs(sum(nums[:maxy+1])-sum(nums[maxy+1:]))
        d1=abs(sum(nums[:maxy])-sum(nums[maxy:]))
        d2=abs(sum(nums[:maxy+1])-sum(nums[maxy+1:]))
        return min(d1,d2)