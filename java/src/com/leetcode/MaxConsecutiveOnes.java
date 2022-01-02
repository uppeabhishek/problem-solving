package com.leetcode;

/**
 * @author abhishekuppe
 */
public class MaxConsecutiveOnes {
    public int findMaxConsecutiveOnes(int[] nums) {
        int cnt = 0;
        int maxCnt = 0;

        for (int num : nums) {
            if (num == 1) {
                cnt += 1;
            } else {
                if (cnt > maxCnt) {
                    maxCnt = cnt;
                    cnt = 0;
                }
            }
        }

        return maxCnt;
    }
}
