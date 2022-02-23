package com.leetcode;

/**
 * @author abhishekuppe
 */
public class MinCostClimbingStairs {

    public static void main(String[] args) {
        MinCostClimbingStairs minCostClimbingStairs = new MinCostClimbingStairs();
        minCostClimbingStairs.minCostClimbingStairs(new int[]{10, 15, 20});
        minCostClimbingStairs.minCostClimbingStairs(new int[]{1, 100, 1, 1, 1, 100, 1, 1, 100, 1});
    }

//    public int helper(int i, int[] cost, HashMap<Integer, Integer> hashMap) {
//        if (hashMap.containsKey(i)) {
//            return hashMap.get(i);
//        }
//        hashMap.put(i, cost[i] + Math.min(helper(i - 1, cost, hashMap), helper(i - 2, cost, hashMap)));
//        return hashMap.get(i);
//    }

//    public int minCostClimbingStairs(int[] cost) {
//        HashMap<Integer, Integer> hashMap = new HashMap<>();
//        hashMap.put(0, cost[0]);
//        hashMap.put(1, cost[1]);
//
//        helper(cost.length - 1, cost, hashMap);
//        return Math.min(hashMap.get(cost.length - 1), hashMap.get(cost.length - 2));
//    }

    public int minCostClimbingStairs(int[] cost) {
        int[] dp = new int[cost.length];
        dp[0] = cost[0];
        dp[1] = cost[1];

        for (int i = 2; i < cost.length; i++) {
            dp[i] = cost[i] + Math.min(cost[i - 1], cost[i - 2]);
        }

        return Math.min(dp[cost.length - 1], dp[cost.length - 2]);
    }
}
