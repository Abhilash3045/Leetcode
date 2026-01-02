class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        h={};n=len(nums)//2
        for i in nums:
            h[i]=h.get(i,0)+1
        for i in h:
            if h[i]==n:
                return i