class Solution {
    public int getCommon(int[] nums1, int[] nums2) {
        int n1=nums1.length, n2=nums2.length;
        int l=0, r=0;
        while(l<n1 & r<n2){
            if(nums1[l]==nums2[r])  return nums1[l];
            else if(nums1[l]>nums2[r])  r+=1;
            else    l+=1;
        }
        return -1;
    }
}