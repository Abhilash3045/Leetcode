class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        n=[]
        for i in range(len(nums)):
            t=[]
            while nums[i]>0:
               l=nums[i]%10
               t=[l]+t
               nums[i]//=10
            n+=t
        return n