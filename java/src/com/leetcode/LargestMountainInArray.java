package com.leetcode;

/**
 * @author abhishekuppe
 * @link https://leetcode.com/problems/longest-mountain-in-array/
 */
public class LargestMountainInArray {

    public static void main(String[] args) {
        LargestMountainInArray largestMountainInArray = new LargestMountainInArray();
//        largestMountainInArray.longestMountain(new int[] {2,1,4,7,3,2,5});
//        largestMountainInArray.longestMountain(new int[] {2,2,2});
//        largestMountainInArray.longestMountain(new int[] {1, 3, 1, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5});
//        largestMountainInArray.longestMountain(new int[] {0,1,2,3,4,5,6,7,8,9});
//        largestMountainInArray.longestMountain(new int[] {9,8,7,6,5,4,3,2,1,0});
//        largestMountainInArray.longestMountain(new int[] {9,8,7,6,5,4,3,2,1,2});
//        largestMountainInArray.longestMountain(new int[] {0,1,2,3,4,5,6,7,8,9,1});
//        largestMountainInArray.longestMountain(new int[] {9,8,7,6,5,4,3,2,1,0,1});
//        largestMountainInArray.longestMountain(new int[] {2,3,1,2,3,4,5,6});
        largestMountainInArray.longestMountain(new int[]{0, 2, 0, 2, 1, 2, 3, 4, 4, 1});
        largestMountainInArray.longestMountain(new int[]{2, 3, 3, 2, 0, 2});
    }

    public int longestMountain(int[] arr) {
        if (arr.length < 3) {
            return 0;
        }

        boolean shouldIncrease = true;
        int i = 0;
        int actualCnt = 1;
        int previousDownwardIndex = 0;
        boolean isIncreased = false;
        boolean isDecreased = false;
        boolean toReset = false;

        while (i < arr.length - 1) {
            if (arr[i] == arr[i + 1]) {
                previousDownwardIndex = i + 1;
                isIncreased = false;
                isDecreased = false;
                toReset = true;
            } else {
                if (arr[i] < arr[i + 1]) {
                    if (!isIncreased) {
                        isIncreased = true;
                    }
                    if (!shouldIncrease) {
                        actualCnt = Math.max(i - previousDownwardIndex + 1, actualCnt);
                        shouldIncrease = true;
                        previousDownwardIndex = i;
                    }
                } else {
                    if (i == 0 || !isIncreased) {
                        previousDownwardIndex = i + 1;
                    } else {
                        actualCnt = Math.max((i + 1) - previousDownwardIndex + 1, actualCnt);
                        if (shouldIncrease) {
                            shouldIncrease = false;
                        }
                    }
                    if (!isDecreased) {
                        isDecreased = true;
                    }
                }
            }
            i += 1;
        }

        if ((!isDecreased || !isIncreased) && !toReset) {
            return 0;
        }

        if (actualCnt > 2) {
            return actualCnt;
        }
        return 0;
    }
}
