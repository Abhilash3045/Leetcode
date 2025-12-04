public class Solution {
    public long[] SumOfThree(long num) {
        List<long> res = new List<long>();
        if((num-3)%3==0){
            long x = (num-3)/3;
            res.Add(x);
            res.Add(x+1);
            res.Add(x+2);
        }
        return res.ToArray();
    }
}