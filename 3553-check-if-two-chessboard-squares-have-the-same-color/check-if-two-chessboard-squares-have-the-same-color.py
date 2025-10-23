alp = 'abcdefgh'
num = '12345678'
def color(a):
    m = 0
    for i in range(len(alp)):
        if a[0] == alp[i]:
            if i % 2 == 0:
                m += 2
            else:
                m += 1
        if a[1] == num[i]:
            if i % 2 == 0:
                m += 2
            else:
                m += 1
    if m % 2 == 0:
        return "Black"
    else:
        return "White"

class Solution(object):
    def checkTwoChessboards(self, coordinate1, coordinate2):
        """
        :type coordinate1: str
        :type coordinate2: str
        :rtype: bool
        """
        coordinate1 = color(coordinate1)
        coordinate2 = color(coordinate2)
        if coordinate1 == coordinate2:
            return True
        else:
            return False
        