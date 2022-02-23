import java.util.*;

// Definition for singly-linked list.
public class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    private ListNode frontPointer;

    private boolean recursivelyCheck(ListNode cur) {
        if (cur != null) {
            if (!recursivelyCheck(cur.next)) return false;
            if (cur.val != frontPointer.val) return false;
            frontPointer = frontPointer.next;
        }
        return true;
    }

    public boolean isPalindrome(ListNode head) {
        frontPointer = head;
        return recursivelyCheck(head);        
    }

    public static void main(String[] args) {
        System.out.println();
    }
}
