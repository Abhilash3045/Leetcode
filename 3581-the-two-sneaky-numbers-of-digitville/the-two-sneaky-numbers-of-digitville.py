class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        h=set()
        for i in nums:
            if nums.count(i)>1:
                h.add(i)
        return list(h)