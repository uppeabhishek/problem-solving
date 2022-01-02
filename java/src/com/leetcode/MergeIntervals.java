package com.leetcode;

import java.util.Arrays;

/**
 * @author abhishekuppe
 */
public class MergeIntervals {
    public static void main(String[] args) {
        MergeIntervals mergeIntervals = new MergeIntervals();
        mergeIntervals.merge(new int[][]{{1, 3}, {2, 6}, {8, 10}, {15, 18}});
//        mergeIntervals.merge(new int[][]{{1,4}, {2,3}});
//        mergeIntervals.merge(new int[][]{{2,3},{4,5},{6,7},{8,9},{1,10}});
//        mergeIntervals.merge(new int[][]{{1,4}, {4,5}, {5, 6}, {6, 20}});
    }

    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> {
            if (a[0] < b[0]) {
                return -1;
            } else if (a[0] > b[0]) {
                return 1;
            }
            return 0;
        });

        int[][] result = new int[intervals.length][2];

        int index = 0;
        int previousIndex = 0;

        for (int i = 0; i < intervals.length; i++) {
            if (intervals[previousIndex][1] <= intervals[i][0]) {
                result[index][0] = intervals[previousIndex][0];
                result[index][1] = intervals[i - 1][1];
                previousIndex = i;
                index++;
            } else {
                if (i == intervals.length - 1) {
                    result[index][0] = intervals[previousIndex][0];
                    result[index][1] = intervals[previousIndex][1];
                    previousIndex = i;
                    index++;
                }
            }
        }

        return Arrays.copyOfRange(result, 0, index);
    }
}
