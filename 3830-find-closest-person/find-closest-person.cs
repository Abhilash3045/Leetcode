public class Solution {
    public int FindClosest(int x, int y, int z) {
        int first=0,second=0;
        if(x>z){
            first=x-z;
        }
        else if(x<z){
            first=z-x;
        }
        if(y>z){
            second=y-z;
        }
        else if(y<z){
            second=z-y;
        }
        if(first>second){
            return 2;
        }
        else if(first<second){
            return 1;
        }
        else{
            return 0;
        }
    }
}