package com.leetcode;

/**
 * @author abhishekuppe
 * @link https://leetcode.com/problems/count-and-say/
 */
public class CountAndSay {

    public static void main(String[] args) {
        CountAndSay countAndSay = new CountAndSay();
        countAndSay.countAndSay(10);
    }

    public String countAndSay(int n) {
        if (n == 1) {
            return "1";
        }

        int i = 1;
        String result = "1";

        while (i < n) {
            StringBuilder temp = new StringBuilder();
            int cnt = 1;
            char ch = result.charAt(0);
            int j = 0;

            while (true) {
                if (j + 1 == result.length()) {
                    temp.append(cnt).append(ch);
                    result = temp.toString();
                    break;
                }

                if (result.charAt(j) != result.charAt(j + 1)) {
                    temp.append(cnt).append(ch);
                    cnt = 1;
                    ch = result.charAt(j + 1);
                } else {
                    cnt += 1;
                }


                j += 1;
            }
            i++;
        }

        return result;
    }
}
