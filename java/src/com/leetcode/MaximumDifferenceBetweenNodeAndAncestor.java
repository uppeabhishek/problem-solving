package com.leetcode;

/**
 * @author abhishekuppe
 */

public class MaximumDifferenceBetweenNodeAndAncestor {

    int result = 0;
    int minValue = 0;
    int maxValue = 0;

    public static void main(String[] args) {
        MaximumDifferenceBetweenNodeAndAncestor maximumDifferenceBetweenNodeAndAncestor =
                new MaximumDifferenceBetweenNodeAndAncestor();

        TreeNode treeNode = new TreeNode(8);
        treeNode.left = new TreeNode(3);
        treeNode.left.left = new TreeNode(1);
        treeNode.left.right = new TreeNode(6);
        treeNode.left.right.left = new TreeNode(4);
        treeNode.left.right.right = new TreeNode(7);
        treeNode.right = new TreeNode(10);
        treeNode.right.right = new TreeNode(14);
        treeNode.right.right.left = new TreeNode(13);

//        TreeNode treeNode = new TreeNode(1);
//        treeNode.right = new TreeNode(2);
//        treeNode.right.right = new TreeNode(0);
//        treeNode.right.right.left = new TreeNode(3);

//        TreeNode treeNode = new TreeNode(8);
//        treeNode.right = new TreeNode(1);
//        treeNode.right.left = new TreeNode(5);
//        treeNode.right.left.right = new TreeNode(4);
//        treeNode.right.left.left = new TreeNode(2);
//        treeNode.right.left.left.left = new TreeNode(7);
//        treeNode.right.left.left.right = new TreeNode(3);
//        treeNode.right.right = new TreeNode(6);
//        treeNode.right.right.left = new TreeNode(0);

        maximumDifferenceBetweenNodeAndAncestor.maxAncestorDiff(treeNode);
    }

    public void helper(TreeNode root) {

        if (root == null) {
            return;
        }

        result = Math.max(result, Math.max(Math.abs(root.val - maxValue), Math.abs(root.val - minValue)));
        maxValue = Math.max(maxValue, root.val);
        minValue = Math.min(minValue, root.val);
        helper(root.left);
        helper(root.right);
    }

    public int maxAncestorDiff(TreeNode root) {
        minValue = root.val;
        maxValue = root.val;
        helper(root);
        return result;
    }
}
