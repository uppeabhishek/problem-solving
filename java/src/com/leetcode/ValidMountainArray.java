package com.leetcode;

/**
 * @author abhishekuppe
 * @link https://leetcode.com/problems/valid-mountain-array/
 */
public class ValidMountainArray {

    public static void main(String[] args) {
        ValidMountainArray validMountainArray = new ValidMountainArray();
        validMountainArray.validMountainArray(new int[]{0, 3, 2, 1});
    }

    public boolean validMountainArray(int[] arr) {
        if (arr.length < 3) {
            return false;
        }
        boolean shouldIncrease = true;
        int i = 0;
        while (i < arr.length - 1) {
            if (arr[i] == arr[i + 1]) {
                return false;
            } else {
                if (arr[i] < arr[i + 1]) {
                    if (!shouldIncrease) {
                        return false;
                    }
                } else {
                    if (i == 0) {
                        return false;
                    }
                    if (shouldIncrease) {
                        shouldIncrease = false;
                    }
                }
                i += 1;
            }
        }

        return !shouldIncrease;
    }
}
