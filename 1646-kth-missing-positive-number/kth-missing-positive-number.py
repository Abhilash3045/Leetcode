class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        c=0;n=arr[-1]+k
        for i in range(1,n+1):
            if not i in arr:
                c+=1
                if c==k: return i