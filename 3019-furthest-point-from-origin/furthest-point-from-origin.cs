public class Solution {
    public int FurthestDistanceFromOrigin(string moves) {
        int l=0,r=0,d=0;
        foreach(char i in moves){
            if(i=='L')
                l++;
            else if(i=='R')
                r++;
            else
                d++;
        }
        if(l>=r)
            return (l+d)-r;
        else
            return (r+d)-l;
    }
}