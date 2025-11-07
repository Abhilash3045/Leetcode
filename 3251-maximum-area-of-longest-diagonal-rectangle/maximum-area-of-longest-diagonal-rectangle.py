class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        """
        :type dimensions: List[List[int]]
        :rtype: int
        """
        temp=0
        ans=0
        for x,y in dimensions:
            l=x*x+y*y
            a=x*y
            if l>temp:
                temp=l
                ans=a
            elif l==temp:
                ans=max(ans,a)
        return ans