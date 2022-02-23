package com.leetcode;

/**
 * @author abhishekuppe
 */
public class DetectCapital {
    public boolean detectCapitalUse(String word) {

        boolean isFirstLetterCapital = false;
        boolean isNextLetterCapital = false;
        boolean isLetterSmall = false;

        for (int i = 0; i < word.length(); i++) {
            int c = word.charAt(i);
            if (c >= 65 && c <= 90) {
                if (i == 0) {
                    isFirstLetterCapital = true;
                } else {
                    isNextLetterCapital = true;
                    if (isLetterSmall) {
                        return false;
                    }
                }
            } else {
                if (isNextLetterCapital) {
                    return false;
                }
                isLetterSmall = true;
            }
        }

        return isFirstLetterCapital || isLetterSmall;
    }
}
