package com.leetcode;

/**
 * @author abhishekuppe
 */
public class SwapNodesInPairs {

    public static void main(String[] args) {
        SwapNodesInPairs swapNodesInPairs = new SwapNodesInPairs();

        ListNode listNode = new ListNode(1);
        listNode.next = new ListNode(2);
        listNode.next.next = new ListNode(3);
        listNode.next.next.next = new ListNode(4);

        swapNodesInPairs.swapPairs(listNode);
    }

    public ListNode swapPairs(ListNode head) {
        if (head == null) {
            return null;
        }

        ListNode newHead = head;

        ListNode prev = head;
        ListNode current = head;
        ListNode next = head.next;

        while (next != null) {

            ListNode temp = next.next;
            current.next.next = current;

            if (newHead == head) {
                newHead = current.next;
            } else {
                prev.next = current.next;
            }

            current.next = temp;

            if (temp == null) {
                break;
            }

            prev = current;
            current = temp;
            next = current.next;
        }

        return newHead;
    }

//    public void helper(ListNode head) {
//        if (head == null || head.next == null) {
//            return;
//        }
//
//        ListNode temp = head.next.next;
//        head.next.next = head;
//        helper(temp);
//    }
//
//    public ListNode swapPairs(ListNode head) {
//        helper(head);
//        return null;
//    }
}
