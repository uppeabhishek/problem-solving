package com.leetcode;

/**
 * @author abhishekuppe
 * @link https://leetcode.com/problems/is-subsequence/
 */
public class IsSubSequence {
    public static void main(String[] args) {
        IsSubSequence isSubSequence = new IsSubSequence();
        isSubSequence.isSubsequence("abc", "ahbgdc");
        isSubSequence.isSubsequence("axc", "ahbgdc");
    }

    public boolean isSubsequence(String s, String t) {
        int i = 0, j = 0;

        while (i < s.length() && j < t.length()) {
            if (s.charAt(i) == t.charAt(j)) {
                i += 1;
            }
            j += 1;
        }

        System.out.println(i == s.length());
        return i == s.length();
    }
}
