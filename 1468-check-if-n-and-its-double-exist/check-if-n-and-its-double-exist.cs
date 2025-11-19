public class Solution {
    public bool CheckIfExist(int[] arr) {
        HashSet<int> s = new HashSet<int>();
        foreach(int i in arr){
            if(s.Contains(2*i) || (i%2==0 && s.Contains(i/2))){
                return true;
            }
            s.Add(i);
        }
        return false;
    }
}