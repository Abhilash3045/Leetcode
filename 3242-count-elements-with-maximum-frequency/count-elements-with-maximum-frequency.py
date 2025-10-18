class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n={}
        for num in nums:
            if num in n:
                n[num]+=1
            else:
                n[num]=1
        x=0
        v=max(n.values())
        for i, j in n.items():
            if j==v:
                x+=v
        return x
