package com.leetcode;

import java.util.HashMap;

/**
 * @author abhishekuppe
 */
public class HouseRobber {

    public static void main(String[] args) {
        HouseRobber houseRobber = new HouseRobber();
        houseRobber.rob(new int[]{1, 2, 3, 1});
    }

    public int helper(int i, int[] nums, HashMap<Integer, Integer> hashMap) {
        if (hashMap.containsKey(i)) {
            return hashMap.get(i);
        }

        if (i == 0) {
            return nums[0];
        }

        if (i == 1) {
            return Math.max(nums[0], nums[1]);
        }

        hashMap.put(i, Math.max(helper(i - 1, nums, hashMap), nums[i] + helper(i - 2, nums, hashMap)));
        return hashMap.get(i);
    }

    public int rob(int[] nums) {
        HashMap<Integer, Integer> hashMap = new HashMap<>();
        return helper(nums.length - 1, nums, hashMap);
    }
}
