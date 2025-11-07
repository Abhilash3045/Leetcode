public class Solution {
    public int FindPeakElement(int[] nums) {
        int temp = nums[0];
        int ans = 0;
        for(int i=0;i<nums.Length;i++)
        {
            if(nums[i]>=temp)
            {
                temp = nums[i];
                ans = i;
            }
        }
        return ans;
    }
}