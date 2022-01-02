package com.leetcode;

/**
 * @author abhishekuppe
 */

class Node {
    int data;
    Node next;

    public Node(int d) {
        data = d;
        next = null;
    }
}

class MyLinkedList {

    Node head;

    public MyLinkedList() {
        head = null;
    }

    public static void main(String[] args) {
        MyLinkedList myLinkedList = new MyLinkedList();
        myLinkedList.addAtHead(1);
        myLinkedList.addAtTail(3);
        myLinkedList.addAtIndex(1, 2);
        myLinkedList.get(1);
        myLinkedList.deleteAtIndex(1);
        myLinkedList.get(1);
        myLinkedList.get(3);
        myLinkedList.deleteAtIndex(3);
        myLinkedList.deleteAtIndex(3);
        myLinkedList.get(0);
        myLinkedList.deleteAtIndex(0);
        myLinkedList.get(0);
    }

    public int get(int index) {
        int cnt = 0;
        Node temp = head;
        while (temp != null && cnt != index) {
            temp = temp.next;
            cnt += 1;
        }

        if (temp == null) {
            return -1;
        }

        return temp.data;
    }

    public void addAtHead(int val) {
        Node temp = new Node(val);
        if (head == null) {
            head = temp;
        } else {
            Node next = head;
            head = temp;
            head.next = next;
        }
    }

    public void addAtTail(int val) {
        if (head == null) {
            addAtHead(val);
        } else {
            Node temp = head;
            while (temp.next != null) {
                temp = temp.next;
            }
            temp.next = new Node(val);
        }
    }

    public void addAtIndex(int index, int val) {
        if (index == 0) {
            addAtHead(val);
        } else {
            int cnt = 0;
            Node temp = head;
            while (temp != null && cnt + 1 < index) {
                temp = temp.next;
                cnt += 1;
            }

            if (cnt + 1 != index || temp == null) {
                return;
            }

            Node next = temp.next;
            temp.next = new Node(val);
            temp.next.next = next;
        }
    }

    public void deleteAtIndex(int index) {
        if (index == 0) {
            if (head != null) {
                head = head.next;
            }
        } else {
            Node temp = head;
            int cnt = 0;
            while (cnt + 1 < index && temp != null) {
                temp = temp.next;
                cnt += 1;
            }

            if (cnt + 1 != index || temp == null || temp.next == null) {
                return;
            }

            temp.next = temp.next.next;

        }
    }
}
