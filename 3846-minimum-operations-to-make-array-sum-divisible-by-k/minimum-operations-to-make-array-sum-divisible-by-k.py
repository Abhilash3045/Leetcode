class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        t=sum(nums)
        if t%k==0:
            return 0
        else:
            return t%k