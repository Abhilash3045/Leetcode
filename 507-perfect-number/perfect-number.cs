public class Solution {
    public bool CheckPerfectNumber(int num) {
        if(num<=1)  return false;
        int res=1;
        int limit = (int)Math.Sqrt(num);
        for(int i=2;i<=limit; i++){
            if(num%i==0){
                res+=i;
                int ott=num/i;
                if(ott!=i){
                    res+=ott;
                }
            }
        }
        return num==res;
    }
}