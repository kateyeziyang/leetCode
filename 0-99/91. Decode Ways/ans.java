import java.util.*;

class Solution {

    public int numDecodings(String s) {
        int n = s.length();
        if (n == 0) return 0;

        // for (int i = n-1; i >= 0; i++) {
        //     if (s.charAt(i) == '0') {
        //         if (i == 0 || s.charAt(i-1) != '1' || s.charAt(i-1) != '2') return 0;
        //     }
        // }

        int[] dp = new int[n];
        if (n > 0) {
            if (s.charAt(n-1) != '0') dp[n-1] = 1;
        }
        if (n > 1) {
            if (s.charAt(n-2) == '1' || (s.charAt(n-2) == '2' && s.charAt(n-1) <= '6')) dp[n-2] += 1;
            if (s.charAt(n-2) != '0') dp[n-2] += 1 * dp[n-1];
        }
        for (int i = n-3; i >= 0; i--) {
            dp[i] = (s.charAt(i) != '0' ? 1 : 0) * dp[i+1];
            int twoDigits = Integer.parseInt(s.substring(i, i+2));
            dp[i] += (twoDigits > 9 && twoDigits < 27 ? 1 : 0) * dp[i+2];
        }

        return dp[0];
    }

    public static void main(String[] args) {
        System.out.println('5');
    }
}
