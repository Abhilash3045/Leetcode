public class Solution {
    public int CountHillValley(int[] nums) {
        List<int> n = new List<int> {nums[0]};
        for(int i = 1; i < nums.Length; i++)
        {
            if(nums[i] != n[n.Count-1])
            {
                n.Add(nums[i]);
            }
        }
        int hills = 0;
        for(int i = 1; i < n.Count-1; i++)
        {
            if(n[i]>n[i-1] && n[i]>n[i+1])
            {
                hills++;
            }
            else if(n[i]<n[i-1] && n[i]<n[i+1])
            {
                hills++;
            }
        }
        return hills;
    }
}