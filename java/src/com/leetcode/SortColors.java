package com.leetcode;

/**
 * @author abhishekuppe
 */
public class SortColors {
    public void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }

    public void sortColors(int[] nums) {
        if (nums.length < 2) {
            return;
        }

        int i = 0, j = 1, k = nums.length - 1;

        while (j < k) {
            if (nums[j] == 0) {
                swap(nums, i, j);
                i += 1;
            } else if (nums[j] == 2) {
                swap(nums, j, k);
                k -= 1;
            } else {
                j += 1;
            }
        }
    }
}
