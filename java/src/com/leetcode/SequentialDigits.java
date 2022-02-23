package com.leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * @author abhishekuppe
 */
public class SequentialDigits {

    public static void main(String[] args) {
        SequentialDigits sequentialDigits = new SequentialDigits();
        sequentialDigits.sequentialDigits(1000, 13000);
    }

    public int getLength(int num) {
        int len = 0;
        while (num > 0) {
            num = num / 10;
            len++;
        }
        return len;
    }

    public List<Integer> sequentialDigits(int low, int high) {
        int lowLength = getLength(low);

        ArrayList<Integer> arrayList = new ArrayList<>();

        while (true) {
            int current = 0;
            int dividend = (int) Math.pow(10, lowLength - 1);
            int numberToAdd = 0;

            boolean shouldBreak = false;

            for (int i = 1; i <= lowLength; i++) {
                current += dividend * i;
                numberToAdd += dividend;
                dividend = dividend / 10;
            }

            if (current > high) {
                break;
            }

            if (current >= low) {
                arrayList.add(current);
            }

            int i = 0;
            while (i < 10 - lowLength - 1) {
                current = current + numberToAdd;
                if (current > high) {
                    shouldBreak = true;
                    break;
                }
                if (current >= low) {
                    arrayList.add(current);
                }
                i++;
            }

            if (shouldBreak) {
                break;
            }

            lowLength++;
        }

        return arrayList;
    }
}
