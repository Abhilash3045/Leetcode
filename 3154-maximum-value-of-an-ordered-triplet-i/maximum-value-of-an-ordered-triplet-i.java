class Solution {
    public long maximumTripletValue(int[] nums) {
        int ml=nums[0], md=0;
        long ans=0;
        for(int i=1; i<nums.length; i++){
            ans=Math.max(ans, (long)md*nums[i]);
            md=Math.max(md, ml-nums[i]);
            ml=Math.max(ml, nums[i]);
        }
        return ans;
    }
}