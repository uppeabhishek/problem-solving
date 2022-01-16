package com.leetcode;

/**
 * @author abhishekuppe
 * @link https://leetcode.com/problems/merge-k-sorted-lists/
 */
public class MergeKSortedLists {

    public static void main(String[] args) {
        MergeKSortedLists mergeKSortedLists = new MergeKSortedLists();

        ListNode listNode1 = new ListNode(1);
        listNode1.next = new ListNode(4);
        listNode1.next.next = new ListNode(5);

        ListNode listNode2 = new ListNode(1);
        listNode2.next = new ListNode(3);
        listNode2.next.next = new ListNode(4);

        ListNode listNode3 = new ListNode(2);
        listNode3.next = new ListNode(6);

        ListNode listNode4 = new ListNode(1);
        listNode4.next = new ListNode(2);
        listNode4.next.next = new ListNode(3);

        ListNode listNode5 = new ListNode(1);
        listNode5.next = new ListNode(2);
        listNode5.next.next = new ListNode(3);

        ListNode listNode6 = new ListNode(1);
        listNode6.next = new ListNode(2);
        listNode6.next.next = new ListNode(3);

        ListNode listNode7 = new ListNode(1);
        listNode7.next = new ListNode(2);
        listNode7.next.next = new ListNode(3);

        ListNode listNode8 = new ListNode(1);
        listNode8.next = new ListNode(2);
        listNode8.next.next = new ListNode(3);

        ListNode[] listNodes = new ListNode[]{listNode1, listNode2, listNode3, listNode4};

        ListNode[] listNodes1 = new ListNode[]{listNode1, listNode2, listNode3, listNode4,
                listNode5, listNode6, listNode7, listNode8};

        mergeKSortedLists.mergeKLists(listNodes);
//        mergeKSortedLists.mergeKLists(listNodes1);
    }

    public ListNode merge2Lists(ListNode l1, ListNode l2) {
        if (l1 == null) {
            return l2;
        }

        if (l2 == null) {
            return l1;
        }

        if (l1.val < l2.val) {
            l1.next = merge2Lists(l1.next, l2);
            return l1;
        }

        l2.next = merge2Lists(l1, l2.next);
        return l2;

    }

    public ListNode mergeKLists(ListNode[] lists) {
        if (lists.length == 0) {
            return null;
        }

        if (lists.length == 1) {
            return lists[0];
        }

        int increment = 1;

        while (increment <= lists.length) {
            for (int i = 0; i < lists.length; i += increment * 2) {
                if (i + increment < lists.length) {
                    lists[i] = merge2Lists(lists[i], lists[i + increment]);
                }
            }
            increment = increment * 2;
        }

        return lists[0];
    }
}
