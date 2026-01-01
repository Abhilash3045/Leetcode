class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        h={};s=0
        for i in nums:
            h[i]=h.get(i,0)+1
        for i in h:
            if h[i]==1:
                s+=i
        return s