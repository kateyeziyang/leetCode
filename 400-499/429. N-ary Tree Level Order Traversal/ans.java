import java.util.*;

class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};

// https://leetcode.com/problems/n-ary-tree-level-order-traversal/solution/
class Solution {

    public List<List<Integer>> levelOrder(Node root) {
        List<List<Integer>> result = new ArrayList<>();
        if (root == null) return result;

        List<Node> prevLayer = Arrays.asList(root);
        while (!prevLayer.isEmpty()) {
            List<Node> curLayer = new ArrayList<>();
            List<Integer> prevVals = new ArrayList<>();

            for (Node node: prevLayer) {
                prevVals.add(node.val);
                curLayer.addAll(node.children);
            }
            result.add(prevVals);
            prevLayer = curLayer;
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println();
    }
}
