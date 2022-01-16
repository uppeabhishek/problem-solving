package com.leetcode;

import java.util.Arrays;

/**
 * @author abhishekuppe
 * @link https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
 */
public class MinimumNumberOfArrowsToBurstBalloons {

    public static void main(String[] args) {
        MinimumNumberOfArrowsToBurstBalloons minimumNumberOfArrowsToBurstBalloons =
                new MinimumNumberOfArrowsToBurstBalloons();
        minimumNumberOfArrowsToBurstBalloons.findMinArrowShots(new int[][]{{10, 16}, {2, 8}, {1, 6}, {7, 12}});
//        minimumNumberOfArrowsToBurstBalloons.findMinArrowShots(new int[][]{{1,2}, {3,4}, {5,6}, {7,8}});
//        minimumNumberOfArrowsToBurstBalloons.findMinArrowShots(new int[][]{{1,2},{2,3},{3,4},{4,5}});
//        minimumNumberOfArrowsToBurstBalloons.findMinArrowShots(new int[][]{{3,9},{7,12},{3,8},{6,8},{9,10},{2,9},
//                {0,9}, {3,9},{0,6}, {2,8}});
    }

    public int findMinArrowShots(int[][] points) {

        if (points.length == 1) {
            return 1;
        }

        int i = 0;
        int cnt = 1;

        Arrays.sort(points, (a, b) -> {
            if (a[1] < b[1]) {
                return -1;
            } else if (a[1] > b[1]) {
                return 1;
            } else {
                if (a[0] < b[0]) {
                    return -1;
                } else if (a[0] > b[0]) {
                    return 1;
                }
                return 0;
            }
        });

        int val = points[0][1];

        while (i < points.length - 1) {
            if (val < points[i + 1][0] || val > points[i + 1][1]) {
                val = points[i + 1][1];
                cnt += 1;
            }
            i += 1;
        }

        return cnt;
    }
}
