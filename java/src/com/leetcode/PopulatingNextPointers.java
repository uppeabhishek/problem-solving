package com.leetcode;

/**
 * @author abhishekuppe
 */

class LNode {
    public int val;
    public LNode left;
    public LNode right;
    public LNode next;

    public LNode(int _val) {
        val = _val;
    }

    public LNode(int _val, LNode _left, LNode _right, LNode _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
}

public class PopulatingNextPointers {

    public static void main(String[] args) {
        PopulatingNextPointers populatingNextPointers = new PopulatingNextPointers();

        LNode lNode = new LNode(1);
        lNode.next = null;

        lNode.left = new LNode(2);
        lNode.left.next = null;

        lNode.right = new LNode(3);
        lNode.right.next = null;

        lNode.left.left = new LNode(4);
        lNode.left.left.next = null;

        lNode.left.right = new LNode(5);
        lNode.left.right.next = null;

        lNode.right.left = new LNode(6);
        lNode.right.left.next = null;

        lNode.right.right = new LNode(7);
        lNode.right.right.next = null;

        populatingNextPointers.connect(lNode);
    }

    public void helper(LNode parent, LNode child) {
        if (child == null) {
            return;
        }

        if (parent != null) {
            if (parent.right != null && parent.right != child) {
                child.next = parent.right;
            } else {
                if (parent.next != null) {
                    child.next = parent.next.left;
                }
            }
        }

        helper(child, child.left);
        helper(child, child.right);
    }

    public LNode connect(LNode root) {
        helper(null, root);
        return root;
    }
}
