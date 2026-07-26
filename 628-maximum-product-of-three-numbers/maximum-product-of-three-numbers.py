class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        x=nums[-1]*nums[-2]*nums[-3]; y=nums[0]*nums[1]*nums[-1]
        return x if x>y else y