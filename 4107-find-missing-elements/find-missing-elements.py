class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        r=[]
        miny,maxy=min(nums),max(nums)
        for i in range(miny, maxy):
            if not i in nums:
                r.append(i)
        return r