package com.leetcode;

/**
 * @author abhishekuppe
 * @link https://leetcode.com/problems/complement-of-base-10-integer/
 */
public class ComplementOfBase10Integer {

    public static void main(String[] args) {
        ComplementOfBase10Integer complementOfBase10Integer = new ComplementOfBase10Integer();
        complementOfBase10Integer.bitwiseComplement(5);
    }

    public int bitwiseComplement(int n) {
        String s = Integer.toBinaryString(n);
        StringBuilder res = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '1') {
                res.append('0');
            } else {
                res.append('1');
            }
        }
        return Integer.parseInt(res.toString(), 2);
    }
}
