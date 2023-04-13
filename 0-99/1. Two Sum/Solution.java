import java.util.*;

class Solution {

    public static int[] countBits(int n) {
        int[] ans = new int[n+1];
        for (int i = 0; i <= n; i++) {
            int j = i;
            int count = 0;
            while (j != 0) {
                count += j & 1;
                j >>= 1;
            }
            ans[i] = count;
        }

        return ans;
    }

    public static void main(String[] args) {
        System.out.println("hello");
        System.out.println(countBits(5));
    }
}
