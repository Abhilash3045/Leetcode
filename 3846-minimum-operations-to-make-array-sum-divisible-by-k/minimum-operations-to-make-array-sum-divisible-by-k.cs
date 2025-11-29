public class Solution {
    public int MinOperations(int[] nums, int k) {
        int s = nums.Sum();
        if(s%k==0){
            return 0;
        }
        else{
            return s%k;
        }
    }
}