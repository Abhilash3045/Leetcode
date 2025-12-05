public class Solution {
    public int CountPartitions(int[] nums) {
        int total = nums.Sum();
        int lsum = 0;
        int count = 0;
        for(int i=0;i<nums.Length-1;i++){
            lsum+=nums[i];
            int rsum=total-lsum;
            if((lsum%2)==(rsum%2))
                count++;
        }
        return count;
    }
}