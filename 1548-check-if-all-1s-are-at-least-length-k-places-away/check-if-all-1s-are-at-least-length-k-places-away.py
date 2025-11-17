class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        p=-1
        for i,num in enumerate(nums):
            if num==1:
                if p!=-1 and i-p<=k:
                    return False
                p=i
        return True