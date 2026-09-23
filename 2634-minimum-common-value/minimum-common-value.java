class Solution {
    public int getCommon(int[] nums1, int[] nums2) {
        if (nums1.length > nums2.length) {
            int[] temp = nums1;
            nums1 = nums2;
            nums2 = temp;
        }

        for (int x : nums1) {

            int l = 0;
            int r = nums2.length - 1;

            while (l <= r) {

                int mid = (l + r) / 2;

                if (nums2[mid] == x) {
                    return x;
                }
                else if (nums2[mid] > x) {
                    r = mid - 1;
                }
                else {
                    l = mid + 1;
                }
            }
        }

        return -1;

        // int n1=nums1.length, n2=nums2.length;
        // int l=0, r=0;
        // while(l<n1 & r<n2){
        //     if(nums1[l]==nums2[r])  return nums1[l];
        //     else if(nums1[l]>nums2[r])  r+=1;
        //     else    l+=1;
        // }
        // return -1;
    }
}