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

        System.out.println(diameterOfBinaryTree.diameterOfBinaryTree(treeNode));
    }

    public int helper(TreeNode root, int[] res) {
        if (root == null) {
            return 0;
        }

        int left = helper(root.left, res);
        int right = helper(root.right, res);

        res[0] = Math.max(res[0], left + right);

        return Math.max(left, right) + 1;
    }

    public int diameterOfBinaryTree(TreeNode root) {
        int[] res = new int[1];
        helper(root, res);
        return res[0];
    }
}
