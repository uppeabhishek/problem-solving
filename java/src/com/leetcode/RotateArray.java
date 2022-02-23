package com.leetcode;

/**
 * @author abhishekuppe
 */
public class RotateArray {

    public static void main(String[] args) {
        RotateArray rotateArray = new RotateArray();
        rotateArray.rotate(new int[]{1, 2, 3, 4, 5, 6, 7}, 3);
    }

    public void helper(int[] nums, int i, int j) {
        while (i < j) {
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
            i++;
            j--;
        }
    }

    public void rotate(int[] nums, int k) {
        int k1 = k % nums.length;
        int i = 0, j = nums.length - k1 - 1;

        helper(nums, i, j);

        i = nums.length - k1;
        j = nums.length - 1;

        helper(nums, i, j);

        i = 0;
        j = nums.length - 1;

        helper(nums, i, j);
    }
}
