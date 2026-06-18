class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ml=nums[0];md=0;ans=0
        for i in range(1,len(nums)):
            ans=max(ans,md*nums[i])
            md=max(md,ml-nums[i])
            ml=max(ml,nums[i])
        return ans