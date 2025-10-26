public class Solution {
    public int FindMaxK(int[] nums) {
        Array.Sort(nums);
        int i = nums.Length-1;
        while(i>0)
        {
            if(nums.Contains(-nums[i]))
            {
                return nums[i];
            }
            i--;
        }
        return -1;
    }
}