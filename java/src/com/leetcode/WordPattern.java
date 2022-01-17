package com.leetcode;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Objects;

/**
 * @author abhishekuppe
 * @link https://leetcode.com/problems/word-pattern/
 */
public class WordPattern {

    public static void main(String[] args) {
        WordPattern wordPattern = new WordPattern();
        wordPattern.wordPattern("abba", "dog dog dog dog");
    }

    public boolean wordPattern(String pattern, String s) {
        String[] arr = s.split(" ");

        if (pattern.length() != arr.length) {
            return false;
        }

        HashMap<Character, String> hashMap = new HashMap<>();
        HashSet<String> hashSet = new HashSet<>();

        for (int i = 0; i < pattern.length(); i++) {
            char c = pattern.charAt(i);
            if (!(hashMap.containsKey(c))) {
                if (hashSet.contains(arr[i])) {
                    return false;
                }
                hashMap.put(c, arr[i]);
                hashSet.add(arr[i]);
            } else {
                if (!Objects.equals(hashMap.get(c), arr[i])) {
                    return false;
                }
            }
        }
        return true;
    }

}
