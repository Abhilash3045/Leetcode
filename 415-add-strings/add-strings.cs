public class Solution {
    public string AddStrings(string num1, string num2) {
        BigInteger x = BigInteger.Parse(num1);
        BigInteger y = BigInteger.Parse(num2);
        BigInteger z = x + y;
        return z.ToString();
    }
}