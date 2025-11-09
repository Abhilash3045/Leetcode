class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=int(s,2)
        res=0
        while s>1:
            if s%2==0: s//=2
            else: s+=1
            res+=1
        return res