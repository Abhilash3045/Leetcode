class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        r=[]
        for i in range(len(nums)-1,-1,-1):
            n=nums[i]
            while n:
                d=n%10
                n//=10
                r.append(d)
        r.reverse()
        return r