package com.leetcode;

/**
 * @author abhishekuppe
 */
public class CanPlaceFlowers {

    public static void main(String[] args) {
        CanPlaceFlowers canPlaceFlowers = new CanPlaceFlowers();
        canPlaceFlowers.canPlaceFlowers(new int[]{1, 0, 0, 0, 1}, 1);
    }

    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        if (n == 0) {
            return true;
        }

        for (int i = 0; i < flowerbed.length; i++) {
            if (flowerbed[i] == 0) {
                if (i - 1 < 0) {
                    if (i + 1 == flowerbed.length) {
                        n--;
                    } else {
                        if (flowerbed[i + 1] != 1) {
                            flowerbed[i] = 1;
                            n--;
                        }
                    }
                } else if (i + 1 == flowerbed.length) {
                    if (flowerbed[i - 1] != 1) {
                        flowerbed[i] = 1;
                        n--;
                    }
                } else {
                    if (flowerbed[i - 1] != 1 && flowerbed[i + 1] != 1) {
                        flowerbed[i] = 1;
                        n--;
                    }
                }
            }
            if (n == 0) {
                break;
            }
        }
        return n == 0;
    }
}
