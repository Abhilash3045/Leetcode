class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # low,mid,high=0,0,len(nums)-1
        # while mid<=high:
        #     if nums[mid]==0:
        #         nums[low],nums[mid]=nums[mid],nums[low]
        #         mid+=1
        #         low+=1
        #     elif nums[mid]==1:
        #         mid+=1
        #     else:
        #         nums[mid],nums[high]=nums[high],nums[low]
        #         high-=1
        c0=c1=c2=0
        for num in nums:
            if num==0:
                c0+=1
            elif num==1:
                c1+=1
            else:
                c2+=1
        nums[:]=[0]*c0+[1]*c1+[2]*c2