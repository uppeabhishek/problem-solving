package com.leetcode;

/**
 * @author abhishekuppe
 */
public class NumberWithEvenNumberOfDigits {
    public int findNumbers(int[] nums) {
        int result = 0;
        for (int num : nums) {
            int cnt = 0;
            while (num > 0) {
                num = num / 10;
                cnt += 1;
            }
            if (cnt % 2 == 0) {
                result += 1;
            }
        }
        return result;
    }
}
