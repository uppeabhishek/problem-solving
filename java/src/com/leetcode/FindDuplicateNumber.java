package com.leetcode;

/**
 * @author abhishekuppe
 */
public class FindDuplicateNumber {
    public static void main(String[] args) {
        FindDuplicateNumber findDuplicateNumber = new FindDuplicateNumber();
        findDuplicateNumber.findDuplicate(new int[]{1, 3, 4, 2, 2});
    }

    public int findDuplicate(int[] nums) {
        int current = nums[0];
        while (true) {
            if (nums[current] < 0) {
                for (int i = 0; i < nums.length; i++) {
                    if (nums[i] < 0) {
                        nums[i] = (nums[i] * -2) + nums[i];
                    }
                }
                return current;
            } else {
                int temp = nums[current];
                nums[current] = nums[current] - (nums[current] * 2);
                current = temp;
            }
        }
    }
}
