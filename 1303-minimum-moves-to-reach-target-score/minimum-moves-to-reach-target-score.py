class Solution(object):
    def minMoves(self, target, maxDoubles):
        """
        :type target: int
        :type maxDoubles: int
        :rtype: int
        """
        res=1
        while target>0:
            if not maxDoubles:
                res+=target
                break
            elif target%2==0 and maxDoubles:
                maxDoubles-=1
                target//=2
            else:
                target-=1
            res+=1
        return res-2