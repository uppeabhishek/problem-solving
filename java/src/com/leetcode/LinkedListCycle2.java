package com.leetcode;

import java.util.HashMap;

/**
 * @author abhishekuppe
 */
public class LinkedListCycle2 {

    public static void main(String[] args) {
        LinkedListCycle2 linkedListCycle2 = new LinkedListCycle2();
        linkedListCycle2.detectCycle(null);
    }

    public ListNode detectCycle(ListNode head) {
        HashMap<ListNode, ListNode> hashMap = new HashMap<>();
        while (head != null) {
            if (hashMap.containsKey(head.next)) {
                return head.next;
            }
            hashMap.put(head, head.next);
            head = head.next;
        }
        return null;
    }
}
