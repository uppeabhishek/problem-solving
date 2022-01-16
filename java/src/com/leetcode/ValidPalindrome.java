package com.leetcode;

/**
 * @author abhishekuppe
 * @link https://leetcode.com/problems/valid-palindrome/
 */
public class ValidPalindrome {
    public boolean isPalindrome(String s) {
        StringBuilder stringBuilder = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (Character.isLetter(c) || Character.isDigit(c)) {
                stringBuilder.append(Character.toLowerCase(c));
            }
        }

        int i = 0, j = stringBuilder.length() - 1;
        while (i < j) {
            if (stringBuilder.charAt(i) != stringBuilder.charAt(j)) {
                return false;
            }
            i++;
            j++;
        }
        return true;
    }
}
