package com.leetcode;

/**
 * @author abhishekuppe
 * @link https://leetcode.com/problems/minimum-depth-of-binary-tree/
 */
public class MinimumDepthOfBinaryTree {

    public static void main(String[] args) {
        TreeNode treeNode = new TreeNode(3);
        treeNode.left = new TreeNode(9);
        treeNode.right = new TreeNode(20);
        treeNode.right.left = new TreeNode(15);
        treeNode.right.right = new TreeNode(7);


        TreeNode treeNode1 = new TreeNode(2);
        treeNode1.right = new TreeNode(3);
        treeNode1.right.right = new TreeNode(4);
        treeNode1.right.right.right = new TreeNode(5);
        treeNode1.right.right.right.right = new TreeNode(6);

        MinimumDepthOfBinaryTree minimumDepthOfBinaryTree = new MinimumDepthOfBinaryTree();
        minimumDepthOfBinaryTree.minDepth(treeNode1);
    }

    public int minDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }

        int left = minDepth(root.left);
        int right = minDepth(root.right);

        if (left == 0 && right == 0) {
            return 1;
        } else if (left == 0 || right == 0) {
            return 1 + Integer.max(left, right);
        }
        return 1 + Integer.min(left, right);
    }

}
