public class Solution {
    public int MinNumberOperations(int[] target) {
        int result=target[0];
        for(int i=1; i<target.Length; i++){
            if(target[i]>target[i-1]){
                result+=target[i]-target[i-1];
            }
        }
        return result;
    }
}