public class Solution {
    public long[] SumOfThree(long num) {
        if((num-3)%3!=0)
            return new long[0];
        long[] res = new long[3];
        long i = num/3;
        res[0]=i-1;
        res[1]=i;
        res[2]=i+1;
        return res;
    }
}