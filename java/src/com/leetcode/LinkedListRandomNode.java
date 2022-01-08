package com.leetcode;

import java.util.ArrayList;

/**
 * @author abhishekuppe
 * @link https://leetcode.com/problems/linked-list-random-node/
 */

class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}

public class LinkedListRandomNode {

    ArrayList<Integer> arrayList = new ArrayList<>();

    public LinkedListRandomNode(ListNode head) {
        ListNode temp = head;
        while (temp != null) {
            arrayList.add(temp.val);
            temp = temp.next;
        }
    }

    public static void main(String[] args) {
        ListNode head = new ListNode(1);
        head.next = new ListNode(2);
        head.next.next = new ListNode(3);
        LinkedListRandomNode linkedListRandomNode = new LinkedListRandomNode(head);
        linkedListRandomNode.getRandom();
        linkedListRandomNode.getRandom();
        linkedListRandomNode.getRandom();
        linkedListRandomNode.getRandom();
        linkedListRandomNode.getRandom();
    }

    int getRandomInRange(int min, int max) {
        return (int) Math.floor(Math.random() * (max - min) + min);
    }

    public int getRandom() {
        return arrayList.get(getRandomInRange(1, arrayList.size()) - 1);
    }
}
