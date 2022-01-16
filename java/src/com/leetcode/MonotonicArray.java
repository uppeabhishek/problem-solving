package com.leetcode;

/**
 * @author abhishekuppe
 * @link https://leetcode.com/problems/monotonic-array/
 */
public class MonotonicArray {

    public static void main(String[] args) {
        MonotonicArray monotonicArray = new MonotonicArray();
        monotonicArray.isMonotonic(new int[]{1, 2, 2, 3});
    }

    public boolean isMonotonic(int[] nums) {
        boolean isIncreasing = true;
        boolean hasIncreased = false;
        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] < nums[i + 1]) {
                if (!isIncreasing) {
                    return false;
                }
                hasIncreased = true;
            } else if (nums[i] > nums[i + 1]) {
                if (isIncreasing) {
                    if (hasIncreased) {
                        return false;
                    }
                    isIncreasing = false;
                }
            }
        }
        return true;
    }
}
