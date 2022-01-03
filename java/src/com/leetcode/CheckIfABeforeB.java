package com.leetcode;

/**
 * @author abhishekuppe
 */
public class CheckIfABeforeB {
    public boolean checkString(String s) {
        boolean isB = false;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == 'A' && isB) {
                return false;
            }
            if (s.charAt(i) == 'B') {
                isB = true;
            }
        }
        return true;
    }
}
