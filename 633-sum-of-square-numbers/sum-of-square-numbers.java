class Solution {
    public boolean judgeSquareSum(int c) {
        for(int div=2; div*div<=c; div++){
            if(c%div==0){
                int ec=0;
                while(c%div==0){
                    ec++;
                    c/=div;
                }
                if(div%4==3 && ec%2!=0) return false;
            }
        }
        return c%4!=3;
    }
}