class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        r=[];n=len(nums2)
        for i in nums1:
            j=nums2.index(i)
            while j<n:
                if nums2[j]>i:
                    r.append(nums2[j])
                    comp=nums2[j]
                    break
                if j==n-1:
                    r.append(-1)
                j+=1
        return r