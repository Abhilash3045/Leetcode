class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        res=['999','888','777','666','555','444','333','222','111','000']
        for i in res:
            if i in num:
                return i
        return ""