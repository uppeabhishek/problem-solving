package com.leetcode;

import java.util.Arrays;

/**
 * @author abhishekuppe
 * @link https://leetcode.com/problems/car-pooling/
 */
public class CarPooling {
    public static void main(String[] args) {
        CarPooling carPooling = new CarPooling();
        carPooling.carPooling(new int[][]{{2, 1, 5}, {3, 3, 7}}, 4);
        carPooling.carPooling(new int[][]{{2, 2, 6}, {2, 4, 7}, {8, 6, 7}}, 11);
    }

    public boolean carPooling(int[][] trips, int capacity) {

        int[] result = new int[1001];
        for (int[] trip : trips) {
            result[trip[1]] += trip[0];
            result[trip[2]] -= trip[0];
        }

        System.out.println(Arrays.toString(result));

        int output = 0;
        for (int res : result) {
            output += res;
            if (output > capacity) {
                return false;
            }
        }
        return true;
    }
}
