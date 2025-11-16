class Solution(object):
    def numSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        c=0;res=0
        for i in s:
            if i=='1':
                c+=1
                res+=c
            else:
                c=0
        return res%1000000007