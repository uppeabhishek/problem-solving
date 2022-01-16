package com.leetcode;

import java.util.ArrayList;

/**
 * @author abhishekuppe
 * @link https://leetcode.com/problems/maximize-distance-to-closest-person/
 */
public class MaximumDistanceToClosestPerson {

    public static void main(String[] args) {
        MaximumDistanceToClosestPerson maximumDistanceToClosestPerson = new MaximumDistanceToClosestPerson();
//        maximumDistanceToClosestPerson.maxDistToClosest(new int[] {1,0,0,0,1,0,1});
//        maximumDistanceToClosestPerson.maxDistToClosest(new int[] {1,0,0,0});
//        maximumDistanceToClosestPerson.maxDistToClosest(new int[] {0,1});
//        maximumDistanceToClosestPerson.maxDistToClosest(new int[]{0,1,0,1,0});
//        maximumDistanceToClosestPerson.maxDistToClosest(new int[]{1,1,1,1,0,1});
//        maximumDistanceToClosestPerson.maxDistToClosest(new int[]{0, 1, 1, 0, 1, 1, 1, 0, 1});
        maximumDistanceToClosestPerson.maxDistToClosest(new int[]{0, 1, 0, 0, 0, 1, 1, 0, 1, 1});
    }

    public int maxDistToClosest(int[] seats) {
        int maxValue = 1;
        ArrayList<Integer> arrayList = new ArrayList<>();

        for (int i = 0; i < seats.length; i++) {
            if (seats[i] == 1) {
                arrayList.add(i);
            }
        }

        int first = 0, second = 1;
        int size = 2;
        boolean isFirst = true;

        for (int i = 0; i < seats.length; i++) {
            if (arrayList.size() == 1) {
                maxValue = Integer.max(maxValue, Math.abs(i - arrayList.get(0)));
            } else {
                if (seats[i] == 0) {
                    if (second == -1 || i < arrayList.get(first)) {
                        maxValue = Integer.max(maxValue, Math.abs(i - arrayList.get(first)));
                    } else if (i > arrayList.get(second)) {
                        maxValue = Integer.max(maxValue, Math.abs(i - arrayList.get(second)));
                    } else {
                        maxValue = Integer.max(maxValue,
                                Integer.min(Math.abs(i - arrayList.get(first)), Math.abs(i - arrayList.get(second))));
                    }
                } else {
                    if (isFirst) {
                        isFirst = false;
                        continue;
                    }
                    size += 1;
                    if (size <= arrayList.size()) {
                        first = second;
                        second++;
                    } else {
                        first = second;
                        second = -1;
                    }
                }
            }
        }

        return maxValue;
    }
}
