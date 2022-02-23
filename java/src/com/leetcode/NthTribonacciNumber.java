package com.leetcode;

import java.util.HashMap;

/**
 * @author abhishekuppe
 */
public class NthTribonacciNumber {

    public int helper(int n, HashMap<Integer, Integer> hashMap) {
        if (hashMap.containsKey(n)) {
            return hashMap.get(n);
        }
        if (n == 0) {
            return 0;
        }
        if (n < 3) {
            return 1;
        }

        hashMap.put(n, helper(n - 1, hashMap) + helper(n - 2, hashMap) + helper(n - 3, hashMap));
        return hashMap.get(n);
    }

    public int tribonacci(int n) {
        return helper(n, new HashMap<>());
    }
}
