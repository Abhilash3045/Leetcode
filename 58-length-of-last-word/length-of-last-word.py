class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.rstrip()
        s = list(s.split(' '))
        s = s[-1]
        return len(s)
        