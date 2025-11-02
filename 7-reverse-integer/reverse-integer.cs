public class Solution {
    public int Reverse(int x) {
        string b = x.ToString();
        string c = "";
        string d = "";
        int f = 0;
        if(b[0]=='-')
        {
            c = b.Substring(1);
        }
        else
        {
            c = b;
        }
        for(int i = c.Length-1; i >= 0; i--)
        {
            d += c[i];
        }
        long e = long.Parse(d);
        if(x<0)
        {
            e = -e;
        }
        if(e >= int.MinValue && e <= int.MaxValue-1)
        {
            f = (int)e;
            return f;
        }
        else
        {
            return 0;
        }
    }
}