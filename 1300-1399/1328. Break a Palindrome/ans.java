import java.util.*;

class Solution {
    // only iterate through half of the string because it's a palindrome
    public String breakPalindrome(String palindrome) {
        int n = palindrome.length();
        if (n == 1) return "";

        for (int i = 0; i < n; i++) {
            if (palindrome.charAt(i) != 'a') {
                if (n % 2 == 1 && (i * 2 + 1) == n) continue;
                return palindrome.substring(0, i) + 'a' + palindrome.substring(i + 1);
            }
        }
        return palindrome.substring(0, n - 1) + 'b';
    }
    public static void main(String[] args) {
        System.out.println();
    }
}
