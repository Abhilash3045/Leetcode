class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a={}
        for i in nums:
            if i not in a:
                a.update({i:1})
            else:
                a[i]+=1
        for key, value in a.items():
            if value==1:
                return key