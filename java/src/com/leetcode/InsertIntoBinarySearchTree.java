package com.leetcode;

/**
 * @author abhishekuppe
 * @link https://leetcode.com/problems/insert-into-a-binary-search-tree/
 */


public class InsertIntoBinarySearchTree {

    public void helper(TreeNode root, int val) {
        if (val < root.val) {
            if (root.left == null) {
                root.left = new TreeNode(val);
                return;
            }
            helper(root.left, val);
        } else {
            if (root.right == null) {
                root.right = new TreeNode(val);
                return;
            }
            helper(root.right, val);
        }
    }

    public TreeNode insertIntoBST(TreeNode root, int val) {
        if (root == null) {
            return new TreeNode(val);
        }
        helper(root, val);
        return root;
    }
}
