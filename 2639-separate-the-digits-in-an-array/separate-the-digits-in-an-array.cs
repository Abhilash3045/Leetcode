public class Solution {
    public int[] SeparateDigits(int[] nums) {
        List<int> num = new List<int>();
        for(int i = nums.Length-1; i>=0; i--){
            int n = nums[i];
            while (n>0){
                int d = n%10;
                n/=10;
                num.Add(d);
            }
        }
        num.Reverse();
        return num.ToArray();
    }
}