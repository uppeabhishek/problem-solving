package com.leetcode;

import java.util.*;

/**
 * @author abhishekuppe
 * @link https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
 */
public class BinaryTreeLevelOrderTraversal2 {

    public static void main(String[] args) {
        BinaryTreeLevelOrderTraversal2 binaryTreeLevelOrderTraversal2 = new BinaryTreeLevelOrderTraversal2();
        TreeNode treeNode = new TreeNode(3);
        treeNode.left = new TreeNode(9);
        treeNode.right = new TreeNode(20);
        treeNode.right.left = new TreeNode(15);
        treeNode.right.right = new TreeNode(7);
        binaryTreeLevelOrderTraversal2.levelOrderBottom(treeNode);
    }

    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        if (root == null) {
            return result;
        }

        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        queue.add(null);

        List<Integer> current = new ArrayList<>();

        boolean isQueueNull = false;
        while (!queue.isEmpty()) {
            TreeNode top = queue.poll();
            if (top == null) {
                if (isQueueNull) {
                    break;
                }
                result.add(current);
                current = new ArrayList<>();
                queue.add(null);
                isQueueNull = true;
            } else {
                current.add(top.val);
                if (top.left != null) {
                    queue.add(top.left);
                }
                if (top.right != null) {
                    queue.add(top.right);
                }
                isQueueNull = false;
            }
        }
        Collections.reverse(result);
        return result;
    }
}
