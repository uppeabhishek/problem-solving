package com.leetcode;

import java.util.HashMap;
import java.util.HashSet;

/**
 * @author abhishekuppe
 */
public class FindTheTownJudge {

    public static void main(String[] args) {
        FindTheTownJudge findTheTownJudge = new FindTheTownJudge();
        findTheTownJudge.findJudge(2, new int[][]{{1, 2}});
    }

    public int findJudge(int n, int[][] trust) {
        if (trust.length == 0) {
            if (n == 1) {
                return 1;
            }
            return -1;
        }

        HashMap<Integer, HashSet<Integer>> hashMap = new HashMap<>();

        for (int[] t : trust) {
            int key = t[0];
            int val = t[1];
            if (hashMap.containsKey(key)) {
                hashMap.get(key).add(val);
            } else {
                HashSet<Integer> hashSet1 = new HashSet<>();
                hashSet1.add(val);
                hashMap.put(key, hashSet1);
            }
        }
        int val = -1;
        for (int i = 1; i <= n; i++) {
            if (!hashMap.containsKey(i)) {
                if (val != -1) {
                    return -1;
                }
                val = i;
            }
        }

        if (val == -1) {
            return -1;
        }

        for (HashSet<Integer> hashSet : hashMap.values()) {
            if (!hashSet.contains(val)) {
                return -1;
            }
        }

        return val;
    }
}
