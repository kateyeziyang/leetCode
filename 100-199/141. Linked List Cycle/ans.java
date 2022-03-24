import java.util.*;

class ListNode {
    int val;
    ListNode next;
    ListNode(int x) {
        val = x;
        next = null;
    }
}

class Solution {

    public static boolean hasCycle(ListNode head) {
        if (head==null) return false;
        ListNode slow,fast;
        slow = fast = head;
        while (fast!=null && fast.next!=null) {
            System.out.println("slow: "+slow.val+" fast: "+fast.val);
            slow = slow.next;
            fast = fast.next.next;
            if (slow==fast) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        ListNode a = new ListNode(3);
        ListNode b = new ListNode(2);
        ListNode c = new ListNode(0);
        ListNode d = new ListNode(-4);
        a.next = b;
        b.next = c;
        c.next = d;
        d.next = b;
        System.out.println(hasCycle(a));
    }
}
