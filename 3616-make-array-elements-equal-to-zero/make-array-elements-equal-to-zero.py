class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        t=sum(nums)
        p, a = 0, 0
        for i,x in enumerate(nums):
            s=t-p-x
            if x==0:
                if p==s:
                    a+=2
                elif abs(p-s)==1:
                    a+=1
            p+=x
        return a