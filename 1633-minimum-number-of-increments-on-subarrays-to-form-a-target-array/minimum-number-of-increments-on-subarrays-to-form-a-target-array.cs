public class Solution {
    public int MinNumberOperations(int[] target) {
        int result=0, previous=0;
        foreach(int i in target){
            if(i>previous){
                result+=i-previous;
            }
            previous=i;
        }
        return result;
    }
}