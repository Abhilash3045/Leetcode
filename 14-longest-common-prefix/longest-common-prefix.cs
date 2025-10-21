public class Solution {
    public string LongestCommonPrefix(string[] strs) {
        if(!strs.Any())
        {
            Console.WriteLine("");
        }
        string prefix = strs[0];
        foreach(string s in strs.Skip(1))
        {
            while(!s.StartsWith(prefix))
            {
                prefix = prefix.Substring(0, prefix.Length-1);
                if(!prefix.Any()){
                    Console.WriteLine("");
                    break;
                }
            }
        }
        return prefix;
    }
}