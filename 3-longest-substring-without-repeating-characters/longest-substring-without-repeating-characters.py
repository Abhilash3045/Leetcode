class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        t,m,i="",0,0
        while i<len(s):
            if s[i] not in t:
                t+=s[i]
                i+=1
                m=max(m, len(t))
            elif s[i] in t:
                t=t[1:]
        return m
