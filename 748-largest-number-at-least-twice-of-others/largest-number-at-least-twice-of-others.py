class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        m1=0;m2=0;ind=0
        for i in range(len(nums)):
            if nums[i]>m1:
                m2=m1
                m1=nums[i]
                ind=i
            elif nums[i]>m2:
                m2=nums[i]
        return ind if m1>=2*m2 else -1