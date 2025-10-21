class Solution(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        ap = 0
        alp = 'abcdefgh'
        num = '12345678'
        for i in range(len(alp)):
            if coordinates[0] == alp[i]:
                if i%2 == 0:
                    ap += 2
                else:
                    ap += 1
            if coordinates[1] == num[i]:
                if i%2 == 0:
                    ap += 2
                else:
                    ap += 1
        if ap % 2 == 0:
            return False
        else:
            return True
