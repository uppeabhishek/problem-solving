package com.hackerrank;

import java.util.Scanner;

/**
 * @author abhishekuppe
 */
public class Strings {
    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner s = new Scanner(System.in);
        String first = s.nextLine();
        String second = s.nextLine();

        int a = first.length();
        int b = second.length();

        String isGreater = "No";
        for (int i = 0; i < Math.min(a, b); i++) {
            int a1 = first.charAt(i);
            int b1 = second.charAt(i);
            if (a1 > b1) {
                isGreater = "Yes";
                break;
            } else if (b1 > a1) {
                break;
            }
        }

        System.out.printf("%d\n%s\n%s", a + b, isGreater, Character.toUpperCase(first.charAt(0)) + first.substring(1) +
                " " + Character.toUpperCase(second.charAt(0)) + second.substring(1));
    }
}
