package com.leetcode;

import java.util.Stack;

/**
 * @author abhishekuppe
 * @link https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
 */

public class SumOfRootToLeaf {

    static int finalResult = 0;


    public static void main(String[] args) {
        SumOfRootToLeaf sumOfRootToLeaf = new SumOfRootToLeaf();
        TreeNode TreeNode = new TreeNode(1);
        TreeNode.left = new TreeNode(0);
        TreeNode.right = new TreeNode(1);
        TreeNode.left.left = new TreeNode(0);
        TreeNode.left.right = new TreeNode(1);
        TreeNode.right.right = new TreeNode(1);
        TreeNode.right.left = new TreeNode(0);
        sumOfRootToLeaf.sumRootToLeaf(TreeNode, new Stack<>());
        System.out.println(finalResult);
    }


    public void sumRootToLeaf(TreeNode root, Stack<Integer> stack) {
        if (root == null) {
            return;
        }

        if (root.left == null && root.right == null) {
            stack.add(root.val);
            Stack<Integer> newStack = new Stack<>();

            int result = 0;
            int index = 0;

            while (!stack.isEmpty()) {
                if (stack.peek() == 1) {
                    result += Math.pow(2, index);
                }
                index += 1;
                newStack.add(stack.pop());
            }

            finalResult += result;

            while (!newStack.isEmpty()) {
                stack.push(newStack.pop());
            }

            stack.pop();
        }

        stack.add(root.val);
        sumRootToLeaf(root.left, stack);
        sumRootToLeaf(root.right, stack);
        stack.pop();
    }

}
