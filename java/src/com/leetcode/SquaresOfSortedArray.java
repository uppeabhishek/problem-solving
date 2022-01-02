package com.leetcode;

/**
 * @author abhishekuppe
 */
public class SquaresOfSortedArray {

    public static void main(String[] args) {
        SquaresOfSortedArray squaresOfSortedArray = new SquaresOfSortedArray();
        squaresOfSortedArray.sortedSquares(new int[]{-10, -8, -7, -1});
    }

    public int[] sortedSquares(int[] nums) {
        int[] result = new int[nums.length];
        int frontPointer = -1;
        int backPointer = nums.length;
        int index = 0;
        for (int num : nums) {
            if (num >= 0) {
                backPointer = index;
                frontPointer = index - 1;
                break;
            }
            index += 1;
        }

        if (frontPointer == -1 && backPointer == nums.length) {
            frontPointer = nums.length - 1;
        }

        int resultIndex = 0;

        while (frontPointer > -1 && backPointer < nums.length) {
            if (Math.abs(nums[frontPointer]) <= Math.abs(nums[backPointer])) {
                result[resultIndex++] = nums[frontPointer] * nums[frontPointer];
                frontPointer -= 1;
            } else {
                result[resultIndex++] = nums[backPointer] * nums[backPointer];
                backPointer += 1;
            }
        }

        while (frontPointer > -1) {
            result[resultIndex++] = nums[frontPointer] * nums[frontPointer];
            frontPointer -= 1;
        }


        while (backPointer < nums.length) {
            result[resultIndex++] = nums[backPointer] * nums[backPointer];
            backPointer += 1;
        }

        return result;
    }
}
