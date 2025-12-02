class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        second=0;res=0;zeros=0
        for first in range(len(nums)):
            if nums[first]==0: zeros+=1
            while zeros>1:
                if nums[second]==0: zeros-=1
                second+=1
            res=max(res,first-second)
        return res