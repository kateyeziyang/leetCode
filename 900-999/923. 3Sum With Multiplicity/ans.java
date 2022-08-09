import java.util.*;
class Solution {

    public int threeSumMulti(int[] arr, int target) {
        long[] count = new long[101];
        int uniq = 0;
        for (int x: arr) {
            count[x]++;
            if (count[x] == 1)
                uniq++;
        }

        int[] keys = new int[uniq];
        int t = 0;
        for (int i = 0; i <= 100; ++i)
            if (count[i] > 0)
                keys[t++] = i;
        
        long ans = 0;

        for (int i = 0; i < keys.length; ++i) {
            int x = keys[i];
            int T = target - x;
            int j = i, k = keys.length -1;
            while (j <= k) {
                int y = keys[j], z = keys[k];
                if (y + z < T) {
                    j++;
                } else if (y + z > T) {
                    k--;
                } else {
                    if (i < j && j < k) {
                        ans += count[x] * count[y] * count[z];
                    } else if (i == j && j < k) {
                        ans += count[x] * (count[y]-1)/2 * count[z];
                    } else if (i < j && j == k) {
                        ans += count[x] * count[y] * (count[z]-1)/2;
                    } else {
                        ans += count[x] * (count[y]-1)/2 * (count[z]-2)/3;
                    }

                    ans %= 1_000_000_007;
                    j++;
                    k--;
                }
            }
        }

        return (int) ans;
    }

    public static void main(String[] args) {
        System.out.println();
    }
}
