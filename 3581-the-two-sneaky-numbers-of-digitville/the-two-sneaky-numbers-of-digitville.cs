public class Solution {
    public int[] GetSneakyNumbers(int[] nums) {
        Hashtable table = new Hashtable();
        List<int> res = new List<int>();
        foreach(int n in nums)
        {
            if(table.ContainsKey(n)){
                table[n]=(int)table[n]+1;
            }
            else{
                table[n]=1;
            }
            if((int)table[n]>1){
                res.Add(n);
            }
        }
        return res.ToArray();
    }
}