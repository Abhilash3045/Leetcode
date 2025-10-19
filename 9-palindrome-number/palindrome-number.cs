public class Solution {
    public bool IsPalindrome(int x) {
        string s = x.ToString();
        string t = "";
        for(int i = s.Length - 1 ; i >= 0; i--)
        {
            t += s[i];
        }
        if( t == s ){
            // Console.WriteLine("True");
            return true;
        }
        else{
            // Console.WriteLine("False");
            return false;
        }
        // return bool True;
        // return bool null;
    }
}