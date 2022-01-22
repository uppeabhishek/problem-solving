package com.leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * @author abhishekuppe
 */
public class PascalsTriangle2 {

    public static void main(String[] args) {
        PascalsTriangle2 pascalsTriangle2 = new PascalsTriangle2();
        pascalsTriangle2.getRow(3);
    }

    public int helper(int i, int j, int[][] cache) {
        if (cache[i][j] != 0) {
            return cache[i][j];
        }

        if (i == 0 || j == 0 || i == j) {
            return 1;
        }

        cache[i][j] = helper(i - 1, j - 1, cache) + helper(i - 1, j, cache);
        return cache[i][j];
    }

    public List<Integer> getRow(int rowIndex) {

        int[] result = new int[rowIndex + 1];

        int[][] cache = new int[rowIndex + 1][rowIndex + 1];

        if (rowIndex == 0) {
            result[0] = 1;
        } else {
            result[0] = 1;
            result[rowIndex] = 1;
            for (int i = 1; i < rowIndex; i++) {
                result[i] = helper(rowIndex, i, cache);
            }
        }

        List<Integer> resultantList = new ArrayList<>(result.length);

        for (int ele : result) {
            resultantList.add(ele);
        }

        return resultantList;
    }
}
