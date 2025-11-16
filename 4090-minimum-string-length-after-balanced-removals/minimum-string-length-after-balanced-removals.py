class Solution(object):
    def minLengthAfterRemovals(self, s):
        """
        :type s: str
        :rtype: int
        """
        a=0;b=0
        for i in s:
            if i=='a': a+=1
            else: b+=1
        if a>b: return a-b
        else: return b-a