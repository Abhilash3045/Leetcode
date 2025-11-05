public class Solution {
    public bool IsSameAfterReversals(int num) {
        string one = Convert.ToString(num);
        string rstr = new string(one.Reverse().ToArray());
        int bint = int.Parse(rstr);
        string tstr = Convert.ToString(bint);
        string rtstr = new string(tstr.Reverse().ToArray());
        return num==int.Parse(rtstr);
    }
}