package com.leetcode;

import java.util.ArrayList;

/**
 * @author abhishekuppe
 * @link https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/
 */
public class DivideStringIntoGroupsOfSizeK {

    public static void main(String[] args) {
        DivideStringIntoGroupsOfSizeK divideStringIntoGroupsOfSizeK = new DivideStringIntoGroupsOfSizeK();
        divideStringIntoGroupsOfSizeK.divideString("abcdefghij", 3, 'x');
    }

    public String[] divideString(String s, int k, char fill) {
        ArrayList<String> arrayList = new ArrayList<>();

        int i = 0;

        while (i < s.length()) {
            if (i + k < s.length()) {
                arrayList.add(s.substring(i, i + k));
            } else {
                String sub = s.substring(i);
                StringBuilder s1 = new StringBuilder(sub);
                int extraLength = k - sub.length();
                int i1 = 0;
                while (i1 < extraLength) {
                    s1.append(fill);
                    i1 += 1;
                }
                arrayList.add(s1.toString());
            }
            i = i + k;
        }

        String[] result = new String[arrayList.size()];
        i = 0;
        for (String current : arrayList) {
            result[i++] = current;
        }
        return result;
    }
}
