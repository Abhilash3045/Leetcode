class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        n1=len(nums1);n2=len(nums2)
        l=r=0
        while l<n1 and r<n2:
            if nums1[l]==nums2[r]:
                return nums1[l]
            elif nums1[l]<nums2[r]:
                l+=1
            else:
                r+=1
        return -1