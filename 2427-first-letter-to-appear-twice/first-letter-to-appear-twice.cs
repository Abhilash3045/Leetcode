public class Solution {
    public char RepeatedCharacter(string s) {
        List<int> res = new List<int>();
        for(int i=0; i<s.Length; i++){
            if(res.Contains(s[i]))
                return s[i];
            res.Add(s[i]);
        }
        return 's';
    }
}