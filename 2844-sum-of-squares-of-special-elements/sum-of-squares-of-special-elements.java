class Solution {
    public int sumOfSquares(int[] nums) {
        int n=nums.length;
        int sum=0,l=nums[n-1];
        for(int i=1; i<=n/2; i++){
            if(n%i==0){
                int k=nums[i-1];
                sum+=k*k;
            }
        }
        return sum+(l*l);
    }
}