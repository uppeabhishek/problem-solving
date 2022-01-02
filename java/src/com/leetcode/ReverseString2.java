package com.leetcode;

/**
 * @author abhishekuppe
 */
public class ReverseString2 {

    public static void main(String[] args) {
        ReverseString2 reverseString2 = new ReverseString2();
//        reverseString2.reverseStr("abcdefg", 2);
        reverseString2.reverseStr("abcd", 3);
//        reverseString2.
//                reverseStr("hyzqyljrnigxvdtneasepfahmtyhlohwxmkqcdfehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqlimjkfnqcqnajmebeddqsgl", 39);
    }

    private StringBuilder reverse(String s) {
        StringBuilder newStr = new StringBuilder();
        int i = s.length() - 1;
        while (i > -1) {
            newStr.append(s.charAt(i));
            i -= 1;
        }
        return newStr;
    }

    public String reverseStr(String s, int k) {
        int i = 0;

        StringBuilder result = new StringBuilder();

        if (k >= s.length()) {
            return reverse(s).toString();
        }

        while (true) {
            result.append(reverse(s.substring(i, i + k)));
            if (i + (2 * k) < s.length()) {
                result.append(s, i + k, i + (2 * k));
            } else {
                result.append(s.substring(i + k));
                break;
            }

            i = i + (2 * k);

            if (i + (2 * k) > s.length()) {
                if (s.length() - i < k) {
                    result.append(reverse(s.substring(i)));
                } else {
                    result.append(reverse(s.substring(i, i + k)));
                    result.append(s.substring(i + k));
                }
                break;
            }
        }
        System.out.println(result);
        return result.toString();
    }
}
