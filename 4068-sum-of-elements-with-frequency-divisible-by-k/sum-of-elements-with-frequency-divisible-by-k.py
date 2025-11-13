class Solution(object):
    def sumDivisibleByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n, v ={}, 0
        for i in nums:
            if i in n:
                n[i]+=1
            else:
                n[i]=1
        for i, j in n.items():
            if j%k==0:
                v+=(i*j)
        return v