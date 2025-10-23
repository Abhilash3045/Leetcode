class Solution(object):
    def hasSameDigits(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while len(s)>2:
            st=""
            for i in range(1,len(s)):
                m=(int(s[i-1])+int(s[i]))%10
                st+=str(m)
            s=st
        return s[0]==s[-1]