class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        h,l={},[]
        for i in nums:
            if i in h:
                h[i]+=1
            else:
                h[i]=1
            if h[i]>1:
                l.append(i)
        return l