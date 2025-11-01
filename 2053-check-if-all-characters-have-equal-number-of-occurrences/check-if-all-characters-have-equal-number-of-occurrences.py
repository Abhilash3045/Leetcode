class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        check = {}
        for i in s:
            if i in check:
                check[i] += 1
            else:
                check[i] = 1
        return True if len(set(check.values()))==1 else False