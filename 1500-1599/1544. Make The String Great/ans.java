import java.util.*;

class Solution {

    public String makeGood(String s) {
        Stack<Character> stack = new Stack<>();

        for (char c: s.toCharArray()) {
            if (!stack.isEmpty() && Math.abs(stack.lastElement()-c) == 32)
                stack.pop();
            else
                stack.add(c);
        }

        StringBuilder ans = new StringBuilder();
        for (char c: stack)
            ans.append(c);
        return ans.toString();
    }

    public static void main(String[] args) {
        System.out.println();
    }
}
