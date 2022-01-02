package com.leetcode;

import java.util.HashSet;

/**
 * @author abhishekuppe
 */
public class IntersectionOfTwoArrays {
    public int[] intersection(int[] nums1, int[] nums2) {
        HashSet<Integer> hashSet = new HashSet<>();
        for (Integer num : nums1) {
            hashSet.add(num);
        }
        HashSet<Integer> result = new HashSet<>();

        for (Integer num : nums2) {
            if (hashSet.contains(num)) {
                result.add(num);
            }
        }

        return result.stream().mapToInt(Integer::intValue).toArray();
    }
}
