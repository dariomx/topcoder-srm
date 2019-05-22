class Solution {
    private final static int MOD = (int) (1e9 + 7);

    private int decode1(char x) {
        if (x == '0')
            return 0;
        else if (x == '*')
            return 9;
        else
            return 1;
    }

    private int decode2(char x, char y) {
        if (x == '*' && y == '*') {
            return 15;
        } else if (x == '*' && y != '*') {
            if (y == '0')
                return 2;
            else if (y >= '1' && y <= '6')
                return 2;
            else
                return 1;
        } else if (x != '*' && y == '*') {
            if (x == '1')
                return 9;
            else if (x == '2')
                return 6;
            else
                return 0;
        } else {
            int dx = x - '0';
            int dy = y - '0';
            int num = dx*10 + dy;
            if (num >= 10 && num <= 26)
                return 1;
            else
                return 0;
        }
    }

    public int numDecodings(String s) {
        int n = s.length();
        long[] rec = new long[n+1];
        rec[n] = 1;
        rec[n-1] = decode1(s.charAt(n-1));
        for(int i=n-2; i>=0; i--) {
            rec[i] = (decode1(s.charAt(i)) * rec[i+1]) % MOD;
            if (i < n-1) {
                char x = s.charAt(i);
                char y = s.charAt(i+1);
                rec[i] = (rec[i] + decode2(x, y) * rec[i+2]) % MOD;
            }
        }
        return (int) rec[0];
    }
}