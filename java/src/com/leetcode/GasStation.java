package com.leetcode;

/**
 * @author abhishekuppe
 */
public class GasStation {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int count = 0;
        int maxIndex = Integer.MIN_VALUE;
        int maxValue = Integer.MIN_VALUE;
        boolean shouldUpdate = false;
        int mainCount = 0;

        for (int i = 0; i < gas.length; i++) {
            int diff = gas[i] - cost[i];
            count += diff;
            mainCount += diff;
            if (diff >= 0) {
                if (maxValue == Integer.MIN_VALUE || shouldUpdate) {
                    maxValue = diff;
                    maxIndex = i;
                    count = diff;
                    shouldUpdate = false;
                }
            } else {
                if (count < 0) {
                    shouldUpdate = true;
                }
            }
        }

        if (mainCount < 0) {
            return -1;
        }

        return maxIndex;
    }
}
