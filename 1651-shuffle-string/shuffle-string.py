class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        e = [""]*len(s)
        for i, j in enumerate(indices):
            e[j] = s[i]
        return "".join(e)