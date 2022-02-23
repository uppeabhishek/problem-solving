package com.leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * @author abhishekuppe
 */
public class AllDivisions {
    public static void main(String[] args) {
        AllDivisions allDivisions = new AllDivisions();
        allDivisions.maxScoreIndices(new int[]{0, 0, 1, 0});
        allDivisions.maxScoreIndices(new int[]{0, 0, 0});
        allDivisions.maxScoreIndices(new int[]{1, 1});
        allDivisions.maxScoreIndices(new int[]{1});
        allDivisions.maxScoreIndices(new int[]{0});
    }

    public List<Integer> maxScoreIndices(int[] nums) {
        int i = 0;

        int[] zeros = new int[nums.length];
        int[] ones = new int[nums.length];

        while (i < nums.length) {
            int end = nums.length - i - 1;
            if (nums[i] == 0) {
                zeros[i] = i - 1 < 0 ? 1 : zeros[i - 1] + 1;
            } else {
                zeros[i] = i - 1 < 0 ? 0 : zeros[i - 1];
            }

            if (nums[end] == 1) {
                ones[end] = end + 1 == ones.length ? 1 : ones[end + 1] + 1;
            } else {
                ones[end] = end + 1 == ones.length ? 0 : ones[end + 1];
            }
            i++;
        }

        i = 0;

        int[] result = new int[nums.length + 1];
        result[0] = ones[0];
        int max = result[0];

        while (i < nums.length) {
            int nextIndex = i + 1;
            int sum = 0;
            sum += zeros[i];
            if (i != nums.length - 1) {
                sum += ones[nextIndex];
            }
            max = Integer.max(max, sum);
            result[nextIndex] = sum;
            i++;
        }

        ArrayList<Integer> arrayList = new ArrayList<>();

        for (i = 0; i < result.length; i++) {
            if (result[i] == max) {
                arrayList.add(i);
            }
        }

        return arrayList;
    }
}
