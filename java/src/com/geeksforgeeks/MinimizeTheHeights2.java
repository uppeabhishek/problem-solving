package com.geeksforgeeks;

import java.util.Arrays;

/**
 * @author abhishekuppe
 */
public class MinimizeTheHeights2 {

    public static void main(String[] args) {
        MinimizeTheHeights2 minimizeTheHeights2 = new MinimizeTheHeights2();
//        minimizeTheHeights2.getMinDiff(new int[]{3,9,12,16,20}, 5,3);
//        minimizeTheHeights2.getMinDiff(new int[]{1,5,8,10}, 4,2);
        minimizeTheHeights2.getMinDiff(new int[]{2, 6, 3, 4, 7, 2, 10, 3, 2, 1}, 10, 5);
    }

    int getMinDiff(int[] arr, int n, int k) {
        Arrays.sort(arr);
        for (int i = 0; i < arr.length; i++) {
            int ele = arr[i];
            if (ele <= k) {
                arr[i] = arr[i] + k;
            } else {
                arr[i] = arr[i] - k;
            }
        }

        int minimum = Integer.MAX_VALUE;
        int maximum = Integer.MIN_VALUE;
        for (int ele : arr) {
            if (ele > maximum) {
                maximum = ele;
            }
            if (ele < minimum) {
                minimum = ele;
            }
        }

        return maximum - minimum;
    }
}
