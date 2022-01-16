package com.leetcode;

/**
 * @author abhishekuppe
 * @link https://leetcode.com/problems/invert-binary-tree/
 */
public class InvertBinaryTree {

    public void helper(TreeNode root) {
        if (root == null) {
            return;
        }

        TreeNode temp = root.left;
        root.left = root.right;
        root.right = temp;

        helper(root.left);
        helper(root.right);
    }

    public TreeNode invertTree(TreeNode root) {
        helper(root);
        return root;
    }
}
