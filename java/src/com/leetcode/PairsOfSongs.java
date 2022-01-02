package com.leetcode;

import java.util.HashMap;

/**
 * @author abhishekuppe
 */
public class PairsOfSongs {

    public static void main(String[] args) {
        PairsOfSongs pairsOfSongs = new PairsOfSongs();
//        pairsOfSongs.numPairsDivisibleBy60(new int[]{30, 20, 150, 100, 40});
        pairsOfSongs.numPairsDivisibleBy60(new int[]{60, 60, 60});
    }

    public int numPairsDivisibleBy60(int[] time) {
        HashMap<Integer, Integer> hashMap = new HashMap<>();

        for (int j : time) {
            if (hashMap.containsKey(j % 60)) {
                hashMap.put(j % 60, hashMap.get(j % 60) + 1);
            } else {
                hashMap.put(j % 60, 1);
            }
        }
        int result = 0;
        for (Integer key : hashMap.keySet()) {
            if (key == 0) {
                result += ((hashMap.get(key) - 1) * hashMap.get(key)) / 2;
            } else {
                int value = 60 - key;
                if (hashMap.containsKey(value)) {
                    if (key == value) {
                        result += ((hashMap.get(key) - 1) * hashMap.get(key)) / 2;
                    } else {
                        result += hashMap.get(value) * hashMap.get(key);
                    }
                    hashMap.put(key, 0);
                    hashMap.put(value, 0);
                }
            }
        }
        return result;
    }
}
