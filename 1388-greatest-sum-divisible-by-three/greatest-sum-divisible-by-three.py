class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        nums1=[];nums2=[]
        total=sum(nums)
        nums.sort()
        for i in nums:
            if i%3==1:
                nums1.append(i)
            elif i%3==2:
                nums2.append(i)
        if total%3==0:
            return total
        ans=0
        if total%3==1:
            r1=nums1[0] if nums1 else float('inf')
            r2=nums2[0]+nums2[1] if len(nums2)>1 else float('inf')
            ans=total-min(r1,r2)
        else:
            r1=nums2[0] if nums2 else float('inf')
            r2=nums1[0]+nums1[1] if len(nums1)>1 else float('inf')
            ans=total-min(r1,r2)
        return ans if ans>0 else 0