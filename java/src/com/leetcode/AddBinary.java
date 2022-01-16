package com.leetcode;

/**
 * @author abhishekuppe
 * @link https://leetcode.com/problems/add-binary/
 */
public class AddBinary {

    public static void main(String[] args) {
        AddBinary addBinary = new AddBinary();
//        addBinary.addBinary("11", "1");
//        addBinary.addBinary("1010", "1011");
        addBinary.addBinary("1", "111");
    }

    char helper(StringBuilder stringBuilder, String val, int index, char rem) {
        char remainder = rem;
        while (index >= 0) {
            char c = val.charAt(index);
            if (c == '1') {
                stringBuilder.append(remainder == '1' ? '0' : '1');
            } else {
                stringBuilder.append(remainder);
                remainder = '0';
            }
            index -= 1;
        }
        return remainder;
    }

    public String addBinary(String a, String b) {
        int i = a.length() - 1, j = b.length() - 1;
        char remainder = '0';
        StringBuilder stringBuilder = new StringBuilder();

        while (i >= 0 && j >= 0) {
            char c = a.charAt(i), d = b.charAt(j);
            if ((c == '1' && d == '1') || (c == '0' && d == '0')) {
                stringBuilder.append(remainder);
                remainder = c;
            } else {
                stringBuilder.append(remainder == '0' ? '1' : '0');
            }
            i -= 1;
            j -= 1;
        }

        remainder = helper(stringBuilder, a, i, remainder);
        remainder = helper(stringBuilder, b, j, remainder);

        if (remainder == '1') {
            stringBuilder.append(remainder);
        }

        return stringBuilder.reverse().toString();
    }
}
