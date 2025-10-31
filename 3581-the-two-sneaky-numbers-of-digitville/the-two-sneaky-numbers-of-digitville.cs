public class Solution {
    public int[] GetSneakyNumbers(int[] nums) {
        Dictionary<int,int> dict = new Dictionary<int,int>();
        int[] res= new int[2];
        foreach(int num in nums){
            if(dict.ContainsKey(num)){
                dict[num]++;
            }
            else{
                dict.Add(num, 1);
            }
            if(dict[num]==2){
                res[res[0]==0 ? 0 : 1] = num;
            }
        }
        return res.ToArray();
    }
}