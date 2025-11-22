public class Solution {
    public int MinimumOperations(int[] nums) {
        int d = 0;
        foreach(int i in nums){
            if(i%3 != 0){
                d+=1;
            }
        }
        return d;
    }
}