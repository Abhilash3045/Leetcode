public class Solution {
    public int LongestValidParentheses(string s) {
        Stack<int> stack = new Stack<int>();
        stack.Push(-1);
        int ml = 0;

        for (int i = 0; i < s.Length; i++) {
            if (s[i] == '(') {
                stack.Push(i);
            } else {
                stack.Pop();

                if (stack.Count == 0) {
                    stack.Push(i);
                } else {
                    ml = Math.Max(ml, i - stack.Peek());
                }
            }
        }

        return ml;
    }
}