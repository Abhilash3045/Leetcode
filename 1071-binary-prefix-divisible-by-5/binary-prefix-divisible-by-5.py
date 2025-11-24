class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        res=[];rem=0
        for num in nums:
            rem=(rem*2+num)%5
            res.append(rem==0)
        return res