public class Solution {
    public string Multiply(string num1, string num2) {
        BigInteger a = BigInteger.Parse(num1);
        BigInteger b = BigInteger.Parse(num2);
        BigInteger c = a*b;
        string d = Convert.ToString(c);
        return d;
        // return Convert.ToString(BigInteger.Parse(num1)*BigInteger.Parse(num2));
    }
}