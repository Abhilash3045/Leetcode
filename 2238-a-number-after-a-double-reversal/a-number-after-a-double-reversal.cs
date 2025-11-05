public class Solution {
    public bool IsSameAfterReversals(int num) {
        string one = Convert.ToString(num);
        string rstr = new string(one.Reverse().ToArray());
        BigInteger bint = BigInteger.Parse(rstr);
        string tstr = Convert.ToString(bint);
        string rtstr = new string(tstr.Reverse().ToArray());
        return num==BigInteger.Parse(rtstr);
    }
}