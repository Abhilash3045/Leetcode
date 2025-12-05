class Solution {
    public int countPartitions(int[] nums) {
        int total = 0;
        for(int i = 0; i<nums.length; i++){
            total+=nums[i];
        }
        int lsum = 0;
        int count = 0;
        for(int i=0;i<nums.length-1;i++){
            lsum+=nums[i];
            int rsum=total-lsum;
            if((lsum%2)==(rsum%2))
                count++;
        }
        return count;
    }
}