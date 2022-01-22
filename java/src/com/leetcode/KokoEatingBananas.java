package com.leetcode;

/**
 * @author abhishekuppe
 */
public class KokoEatingBananas {

    public static void main(String[] args) {
        KokoEatingBananas kokoEatingBananas = new KokoEatingBananas();
//        kokoEatingBananas.minEatingSpeed(new int[]{3, 6, 7, 11}, 8);
//        kokoEatingBananas.minEatingSpeed(new int[]{30,11,23,4,20}, 6);
//        kokoEatingBananas.minEatingSpeed(new int[]{122890061, 438301112, 257983174, 614414075, 602060597, 391389864,
//                140358431, 117439906, 992360201, 246252220}, 33212669);
        kokoEatingBananas.minEatingSpeed(new int[]{1000000000, 1000000000}, 3);
    }


    public int minEatingSpeed(int[] piles, int h) {
        int max = Integer.MIN_VALUE;

        for (int pile : piles) {
            if (pile > max) {
                max = pile;
            }
        }

        int low = 1;
        int high = max;
        int mid;

        while (low < high) {
            mid = low + ((high - low) / 2);
            int i = piles.length - 1;
            int currentH = 0;
            while (i >= 0) {
                currentH += (int) Math.ceil((double) piles[i] / mid);
                i--;
            }
            if (currentH <= h) {
                high = mid;
            } else if (currentH > 0) {
                low = mid + 1;
            } else {
                break;
            }
        }

        return high;

    }
}
