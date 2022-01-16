package com.hackerrank;

import java.util.Scanner;

/**
 * @author abhishekuppe
 */
public class Lexicographical {
    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */

        Scanner scanner = new Scanner(System.in);

        String input = scanner.nextLine();
        int k = scanner.nextInt();

        StringBuilder smallest = new StringBuilder();
        StringBuilder largest = new StringBuilder();

        for (int i = 0; i < input.length() - k + 1; i++) {
            StringBuilder temp = new StringBuilder();
            for (int j = i; j < i + k; j++) {
                temp.append(input.charAt(j));
            }

            if (smallest.isEmpty()) {
                smallest = temp;
            } else {
                boolean shouldReplace = false;
                for (int l = 0; l < k; l++) {
                    int a = temp.charAt(l);
                    int b = smallest.charAt(l);

                    if (a < b) {
                        shouldReplace = true;
                        break;
                    } else if (a > b) {
                        break;
                    }
                }
                if (shouldReplace) {
                    smallest = temp;
                }
            }

            if (largest.isEmpty()) {
                largest = temp;
            } else {
                boolean shouldReplace = false;
                for (int l = 0; l < k; l++) {
                    int a = temp.charAt(l);
                    int b = largest.charAt(l);

                    if (a > b) {
                        shouldReplace = true;
                        break;
                    } else if (a < b) {
                        break;
                    }
                }
                if (shouldReplace) {
                    largest = temp;
                }
            }
        }
        System.out.printf("%s\n%s", smallest, largest);
    }
}
