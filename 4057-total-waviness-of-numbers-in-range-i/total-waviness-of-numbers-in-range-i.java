class Solution {
    public int totalWaviness(int num1, int num2) {
        int total = 0;
        for (int x = num1; x <= num2; x++) {
            total += waves(x);
        }
        return total;
    }
    private int waves(int num) {
        String s = String.valueOf(num);
        if (s.length() < 3) {
            return 0;
        }
        int w = 0;
        for (int i = 1; i < s.length() - 1; i++) {
            if ((s.charAt(i) > s.charAt(i - 1) && s.charAt(i) > s.charAt(i + 1)) ||
                (s.charAt(i) < s.charAt(i - 1) && s.charAt(i) < s.charAt(i + 1))) {
                w++;
            }
        }
        return w;
    }
}