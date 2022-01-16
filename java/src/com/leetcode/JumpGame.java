package com.leetcode;

/**
 * @author abhishekuppe
 * @link https://leetcode.com/problems/jump-game/
 */
public class JumpGame {

    public static void main(String[] args) {
        JumpGame jumpGame = new JumpGame();
//        jumpGame.canJump(new int[] {2,3,1,1,4});
//        jumpGame.canJump(new int[] {3,2,1,0,4});
//        jumpGame.canJump(new int[] {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1});
//        jumpGame.canJump(new int[] {0,2,3});
//        jumpGame.canJump(new int[] {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9});
        jumpGame.canJump(new int[]{1, 1, 0, 1});
    }

    public boolean canJump(int[] nums) {
        int nextIndex = 0;
        for (int i = 0; i < nums.length; i++) {
            nextIndex = Math.max(nextIndex, i + nums[i]);
            if (nextIndex < i + 1 && i + 1 < nums.length) {
                return false;
            }
        }
        return true;
    }
}

/*

[2,3,1,1,4]
[3,2,1,0,4]
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
[0,2,3]
[1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
[1,1,0,1]
[0,2,3]
[2,5,0,0]
[3,0,8,2,0,0,1]

 */
