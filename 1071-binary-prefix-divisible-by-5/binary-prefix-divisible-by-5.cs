public class Solution {
    public IList<bool> PrefixesDivBy5(int[] nums) {
        List<bool> flags = new List<bool>();
        int rem=0;
        foreach(int i in nums){
            rem = (rem*2+i)%5;
            flags.Add(rem==0);
        }
        return flags;
    }
}