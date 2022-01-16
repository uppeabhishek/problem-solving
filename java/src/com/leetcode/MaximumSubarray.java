package com.leetcode;

/**
 * @author abhishekuppe
 * @link https://leetcode.com/problems/maximum-subarray/
 */
public class MaximumSubarray {

    public static void main(String[] args) {
        MaximumSubarray maximumSubarray = new MaximumSubarray();
        maximumSubarray.maxSubArray(new int[]{-2, 1, -3, 4, -1, 2, 1, -5, 4});
        maximumSubarray.maxSubArray(new int[]{1});
        maximumSubarray.maxSubArray(new int[]{5, 4, -1, 7, 8});
    }

    public int maxSubArray(int[] nums) {
        int maximumSumTillNow = 0;
        int maximumSum = Integer.MIN_VALUE;

        for (int num : nums) {
            if (maximumSumTillNow + num < 0) {
                maximumSumTillNow = 0;
                maximumSum = Integer.max(maximumSum, maximumSumTillNow + num);
            } else {
                maximumSumTillNow += num;
                maximumSum = Integer.max(maximumSum, maximumSumTillNow);
            }
        }
        return maximumSum;
    }
}
