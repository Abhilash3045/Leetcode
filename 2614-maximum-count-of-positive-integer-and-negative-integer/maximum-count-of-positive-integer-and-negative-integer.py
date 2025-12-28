class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        c=0;n=len(nums);z=0;i=0
        while i<n and nums[i]<1:
            if nums[i]<0: c+=1
            elif nums[i]==0: z+=1
            i+=1
        return max(c,n-c-z)