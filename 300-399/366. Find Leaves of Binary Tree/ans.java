import java.util.*;

class Solution {

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode() {}
        TreeNode(int val) { this.val = val; }
        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

        private List<Pair<Integer, Integer>> pairs;

        public int getHeight(TreeNode root) {
            if (root == null) return -1;

            int leftHeight = getHeight(root.left);
            int rightHeight = getHeight(root.right);

            int curHeight = Math.max(leftHeight, rightHeight) + 1;

            this.pairs.add(new Pair<>(curHeight, root.val));

            return curHeight;
        }

        public List<List<Integer>> findLeaves(TreeNode root) {
            this.pairs = new ArrayList<>();

            getHeight(root);

            Collections.sort(this.pairs, Comparator.comparing(p -> p.getKey()));

            int n = this.pairs.size(), height = 0, i = 0;

            List<List<Integer>> solution = new ArrayList<>();

            while (i < n) {
                List<Integer> nums = new ArrayList<>();
                while (i < n && this.pairs.get(i).getKey() == height) {
                    nums.add(this.pairs.get(i).getValue());
                    i++;
                }
                solution.add(nums);
                height++;
            }
            return solution;
    }

    public static void main(String[] args) {
        System.out.println();
    }
}
