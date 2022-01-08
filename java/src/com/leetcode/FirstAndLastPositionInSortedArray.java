package com.leetcode;

import java.util.Arrays;

/**
 * @author abhishekuppe
 * @link https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
 */
public class FirstAndLastPositionInSortedArray {

    public static void main(String[] args) {
        FirstAndLastPositionInSortedArray firstAndLastPositionInSortedArray = new FirstAndLastPositionInSortedArray();
        firstAndLastPositionInSortedArray.searchRange(new int[]{5, 7, 7, 8, 8, 10}, 8);
    }

    public int[] searchRange(int[] nums, int target) {

        int[] res = new int[]{-1, -1};
        int low = 0, high = nums.length - 1;

        while (low <= high) {
            int mid = (low + high) / 2;
            if (nums[mid] == target) {

                int l, h;

                // left side
                l = 0;
                h = mid;

                while (l <= h) {
                    int m = (l + h) / 2;
                    if (nums[m] != target) {
                        l = m + 1;
                    } else {
                        if (m == 0 || l == h || nums[m - 1] != target) {
                            res[0] = m;
                            break;
                        }
                        h = m - 1;
                    }
                }

                // right side
                l = mid;
                h = nums.length - 1;

                while (l <= h) {
                    int m = (l + h) / 2;
                    if (nums[m] != target) {
                        h = m - 1;
                    } else {
                        if (m == nums.length - 1 || l == h || nums[m + 1] != target) {
                            res[1] = m;
                            break;
                        }
                        l = m + 1;
                    }
                }
                break;
            } else if (target < nums[mid]) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }

        System.out.println(Arrays.toString(res));
        return res;
    }
}
