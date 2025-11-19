public class Solution {
    public int DominantIndex(int[] nums) {
        int max1=0,max2=0,index=0;
        for(int i=0; i<nums.Length; i++){
            if(nums[i]>max1){
                max2=max1;
                max1=nums[i];
                index=i;
            }
            else if(nums[i]>max2){
                max2=nums[i];
            }
        }
        return max1>=2*max2 ? index : -1;
    }
}