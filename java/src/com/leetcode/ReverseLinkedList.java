package com.leetcode;

/**
 * @author abhishekuppe
 */
public class ReverseLinkedList {

    public static void main(String[] args) {
        ReverseLinkedList reverseLinkedList = new ReverseLinkedList();

        ListNode listNode = new ListNode(1);
        listNode.next = new ListNode(2);
        listNode.next.next = new ListNode(3);
        listNode.next.next.next = new ListNode(4);
        listNode.next.next.next.next = new ListNode(5);

        reverseLinkedList.reverseList(listNode);
    }

    // iterative
//    public ListNode reverseList(ListNode head) {
//
//        ListNode prev = null;
//        ListNode current = head;
//        ListNode next;
//
//        while (current != null) {
//            next = current.next;
//            current.next = prev;
//            prev = current;
//            current = next;
//        }
//
//        return prev;
//    }

    // recursive
    public ListNode reverseList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }

        ListNode prev = reverseList(head.next);
        head.next.next = head;
        head.next = null;

        return prev;
    }

}