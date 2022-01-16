package com.leetcode;

/**
 * @author abhishekuppe
 * @link https://leetcode.com/problems/path-sum/
 */

public class PathSum {

    public static void main(String[] args) {
        PathSum pathSum = new PathSum();
//        TreeNode TreeNode = new TreeNode(5);
//        TreeNode.left = new TreeNode(4);
//        TreeNode.left.left = new TreeNode(11);
//        TreeNode.left.left.left = new TreeNode(7);
//        TreeNode.left.left.right = new TreeNode(2);
//        TreeNode.right = new TreeNode(8);
//        TreeNode.right.left = new TreeNode(13);
//        TreeNode.right.right = new TreeNode(4);
//        TreeNode.right.right.right = new TreeNode(1);

        TreeNode TreeNode = new TreeNode(1);
        TreeNode.left = new TreeNode(2);

        pathSum.hasPathSum(TreeNode, 1);
    }


    boolean helper(TreeNode root, int targetSum, int currentSum) {
        if (root == null) {
            return false;
        }

        if (root.left == null && root.right == null) {
            return targetSum == currentSum + root.val;
        }

        return helper(root.left, targetSum, currentSum + root.val) ||
                helper(root.right, targetSum, currentSum + root.val);

    }


    public boolean hasPathSum(TreeNode root, int targetSum) {
        if (root == null) {
            return false;
        }
        return helper(root, targetSum, 0);
    }
}
