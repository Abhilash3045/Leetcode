class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        a = []
        s = list(s.split())
        for i in range(k):
            a += [s[i]]
        return " ".join(a)