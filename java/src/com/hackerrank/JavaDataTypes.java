package com.hackerrank;

import java.math.BigInteger;
import java.util.Scanner;

/**
 * @author abhishekuppe
 */
public class JavaDataTypes {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int count = scanner.nextInt();
        for (int i = 0; i < count; i++) {
            String val = scanner.next();
            BigInteger bigInteger = new BigInteger(val);
            boolean[] result = {false, false, false, false};
            if (bigInteger.longValueExact() >= Byte.MIN_VALUE && bigInteger.longValueExact() <= Byte.MAX_VALUE) {
                result[0] = true;
            }
            if (bigInteger.longValueExact() >= Short.MIN_VALUE && bigInteger.longValueExact() <= Short.MAX_VALUE) {
                result[1] = true;
            }
            if (bigInteger.longValueExact() >= Integer.MIN_VALUE && bigInteger.longValueExact() <= Integer.MAX_VALUE) {
                result[2] = true;
            }
            if (bigInteger.longValueExact() >= Long.MIN_VALUE && bigInteger.longValueExact() <= Long.MAX_VALUE) {
                result[3] = true;
            }

            if (!result[3]) {
                System.out.printf("%s can't be fitted anywhere.\n", val);
            } else {
                System.out.printf("%s can be fitted in:\n", val);
                if (result[0]) {
                    System.out.println("* byte");
                }
                if (result[1]) {
                    System.out.println("* short");
                }
                if (result[2]) {
                    System.out.println("* int");
                }
                if (result[3]) {
                    System.out.println("* long");
                }
            }
        }
    }
}
