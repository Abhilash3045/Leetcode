def binary(x):
    a = ""
    while x > 0:
        a = str(x % 2) + a
        x //= 2
    return a if a else "0"

class Solution(object):
    def convertDateToBinary(self, date):
        """
        :type date: str
        :rtype: str
        """
        year = date[:4]
        month = date[5:7]
        day = date[8:]
        year = binary(int(year))
        month = binary(int(month))
        day = binary(int(day))
        return year + '-' + month + '-' + day
        