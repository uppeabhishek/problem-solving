package com.leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * @author abhishekuppe
 */
public class Subsets {
    public static void main(String[] args) {
        Subsets subsets = new Subsets();
        subsets.subsets(new int[]{1, 2, 3});
    }

    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        for (int i = 0; i < Math.pow(2, nums.length); i++) {
            List<Integer> list = new ArrayList<>();
            String s = Integer.toBinaryString(i);
            int k = 0;
            for (int j = nums.length - s.length(); j < nums.length; j++) {
                if (s.charAt(k) == '1') {
                    list.add(nums[j]);
                }
                k++;
            }
            result.add(list);
        }
        return result;
    }
}
