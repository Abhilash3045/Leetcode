class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        t=sum(nums)
        op=0
        if t%k==0:
            return op
        else:
            return t%k