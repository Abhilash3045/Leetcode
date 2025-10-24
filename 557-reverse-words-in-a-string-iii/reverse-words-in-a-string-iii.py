class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s.split())
        c = []
        for i in s:
            c += [i[::-1]]
        return " ".join(c)