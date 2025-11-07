class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s,t = list(s),list(t)
        for ch in s:
            t.remove(ch)
        return "".join(t)