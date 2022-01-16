package com.leetcode;

/**
 * @author abhishekuppe
 * @link https://leetcode.com/problems/robot-bounded-in-circle/
 */
public class RobotBoundedInTheCircle {

    public static void main(String[] args) {
        RobotBoundedInTheCircle robotBoundedInTheCircle = new RobotBoundedInTheCircle();
        robotBoundedInTheCircle.isRobotBounded("GL");
    }

    public char getDirection(char direction, char instruction) {
        if (instruction == 'L') {
            if (direction == 'N') {
                return 'W';
            } else if (direction == 'W') {
                return 'S';
            } else if (direction == 'S') {
                return 'E';
            }
        } else {
            if (direction == 'N') {
                return 'E';
            } else if (direction == 'E') {
                return 'S';
            } else if (direction == 'S') {
                return 'W';
            }
        }
        return 'N';
    }

    public boolean isRobotBounded(String instructions) {
        int x = 0, y = 0;
        char direction = 'N';

        int cnt = 0;

        while (cnt < 4) {
            for (int i = 0; i < instructions.length(); i++) {
                if (instructions.charAt(i) == 'G') {
                    if (direction == 'N') {
                        y += 1;
                    } else if (direction == 'E') {
                        x += 1;
                    } else if (direction == 'S') {
                        y -= 1;
                    } else {
                        x -= 1;
                    }
                } else {
                    direction = getDirection(direction, instructions.charAt(i));
                }
            }
            cnt += 1;
        }
        return x == 0 && y == 0;
    }
}
