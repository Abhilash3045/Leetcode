class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n=len(nums);s=0;l=nums[-1]
        for i in range(1,n//2+1):
            if n%i==0:
                k=nums[i-1]
                s+=k**2
        return s+(l**2)