package com.leetcode;

import java.util.Arrays;

/**
 * @author abhishekuppe
 * @link https://leetcode.com/problems/jump-game-ii/
 */
public class JumpGame2 {

    public static void main(String[] args) {
        JumpGame2 jumpGame2 = new JumpGame2();
        jumpGame2.jump(new int[]{2, 3, 1, 1, 4});
        jumpGame2.jump(new int[]{1, 2, 1, 1, 1});
    }

    // O(n2)
    public int jump(int[] nums) {
        int[] result = new int[nums.length];
        Arrays.fill(result, Integer.MAX_VALUE);
        result[0] = 0;
        for (int i = 0; i < nums.length; i++) {
            for (int j = 1; j <= nums[i]; j++) {
                int nextIndex = i + j;
                if (nextIndex < nums.length) {
                    result[nextIndex] = Integer.min(result[nextIndex], result[i] + 1);
                }
            }
        }
        return result[nums.length - 1];
    }

    // O(n) todo
//    public int jump(int[] nums) {
//        int[] result = new int[nums.length];
//        Arrays.fill(result, Integer.MAX_VALUE);
//        result[0] = 0;
//
//        int minimumValueTillNow = 0;
//
//        for (int i = 0; i < nums.length; i++) {
//            int nextIndex = i + nums[i];
//            if (nextIndex < nums.length) {
//                if (minimumValueTillNow == 0) {
//                    result[nextIndex] = Math.min(result[nextIndex], 1 + result[i]);
//                    minimumValueTillNow = result[nextIndex];
//                } else {
//                    result[nextIndex] = Math.min(result[nextIndex], minimumValueTillNow + 1);
//                    minimumValueTillNow = result[nextIndex];
//                }
//            }
//        }
//        return -1;
//    }
}
