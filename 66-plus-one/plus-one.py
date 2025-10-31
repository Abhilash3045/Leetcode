class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = int("".join(list(map(str, digits)))) + 1
        a = []
        for i in str(digits):
            a += [i]
        return list(map(int, a))