class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        s=[]
        l=[]
        for i in nums:
            if i in s:
                l.append(i)
            else:
                s.append(i)
        return l