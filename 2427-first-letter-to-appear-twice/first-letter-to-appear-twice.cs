public class Solution {
    public char RepeatedCharacter(string s) {
        HashSet<char> res = new HashSet<char>();
        foreach(char i in s){
            if(res.Contains(i))
                return i;
            res.Add(i);
        }
        return '\0';
    }
}