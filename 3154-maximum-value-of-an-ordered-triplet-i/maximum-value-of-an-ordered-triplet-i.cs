public class Solution {
    public long MaximumTripletValue(int[] nums) {
        int ml = nums[0], md=0;
        long ans=0;
        for(int i=1; i<nums.Length; i++){
            ans=Math.Max(ans, (long)md*nums[i]);
            md=Math.Max(md, ml-nums[i]);
            ml=Math.Max(ml, nums[i]);
        }
        return ans;
    }
}