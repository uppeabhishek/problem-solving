package com.leetcode;

import java.util.Arrays;

/**
 * @author abhishekuppe
 */
public class DestroyingAsteroids {
    public static void main(String[] args) {
        DestroyingAsteroids destroyingAsteroids = new DestroyingAsteroids();
        destroyingAsteroids.asteroidsDestroyed(10, new int[]{3, 9, 19, 5, 21});
    }


    public boolean asteroidsDestroyed(int mass, int[] asteroids) {
        Arrays.sort(asteroids);
        System.out.println(Arrays.toString(asteroids));
        for (int asteroid : asteroids) {
            if (asteroid > mass) {
                return false;
            }
            mass += asteroid;
        }
        return true;
    }
}
