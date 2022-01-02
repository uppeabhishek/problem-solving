package com.leetcode;

import java.util.Arrays;
import java.util.HashMap;

/**
 * @author abhishekuppe
 */
public class TwoSum {
    public static void main(String[] args) {
        TwoSum twoSum = new TwoSum();
        System.out.println(Arrays.toString(twoSum.twoSum(new int[]{3, 3}, 6)));
    }

    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hashmap = new HashMap<>();
        int index = 0;
        int[] res = {-1, -1};
        for (int num : nums) {
            hashmap.put(num, index);
            if (hashmap.containsKey(target - num) && hashmap.get(target - num) != index) {
                res[0] = hashmap.get(target - num);
                res[1] = index;
                break;
            }
            index++;
        }
        return res;
    }
}
