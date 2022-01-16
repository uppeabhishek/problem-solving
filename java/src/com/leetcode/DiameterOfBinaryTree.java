package com.leetcode;

/**
 * @author abhishekuppe
 */
public class DiameterOfBinaryTree {

    public static void main(String[] args) {
        DiameterOfBinaryTree diameterOfBinaryTree = new DiameterOfBinaryTree();
        TreeNode treeNode = new TreeNode(1);
        treeNode.left = new TreeNode(2);
        treeNode.right = new TreeNode(3);
        treeNode.left.left = new TreeNode(4);
        treeNode.left.right = new TreeNode(5);

        TreeNode treeNode1 = new TreeNode(1);
        treeNode1.left = new TreeNode(2);

        TreeNode treeNode2 = new TreeNode(2);
        treeNode2.left = new TreeNode(3);
        treeNode2.left.left = new TreeNode(1);

        System.out.println(diameterOfBinaryTree.diameterOfBinaryTree(treeNode2));
    }

    public int helper(TreeNode root) {
        if (root == null) {
            return 0;
        }

        if (root.left == null && root.right == null) {
            return 1;
        }

        int left = helper(root.left);
        int right = helper(root.right);

        int diameter = left + right;

        System.out.println(diameter + " " + left + " " + right);

        return Integer.max(diameter, Integer.max(left, right));
    }

    public int diameterOfBinaryTree(TreeNode root) {
        if (root == null || (root.left == null && root.right == null)) {
            return 0;
        }
        return helper(root);
    }
}
