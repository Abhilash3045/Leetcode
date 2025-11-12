class Solution(object):
    def findClosest(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """
        first,second=0,0
        if x>=z:
            first=x-z
        elif x<z:
            first=z-x
        if y>=z:
            second=y-z
        elif y<z:
            second=z-y
        if first<second: return 1
        elif first>second: return 2
        else: return 0