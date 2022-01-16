package com.leetcode;

/**
 * @author abhishekuppe
 * @link https://leetcode.com/problems/minimum-moves-to-reach-target-score/
 */
public class MinimumMovesToReachTargetScore {

    public static void main(String[] args) {
        MinimumMovesToReachTargetScore minimumMovesToReachTargetScore = new MinimumMovesToReachTargetScore();
//        minimumMovesToReachTargetScore.minMoves(5, 0);
//        minimumMovesToReachTargetScore.minMoves(19, 2);
        minimumMovesToReachTargetScore.minMoves(766972377, 92);
    }

    public int minMoves(int target, int maxDoubles) {
        if (target == 1) {
            return 0;
        }

        if (maxDoubles == 0) {
            return target - 1;
        }

        int answer = 1;

        if (target % 2 != 0) {
            answer = minMoves(target - 1, maxDoubles);
        } else {
            answer = minMoves(target / 2, maxDoubles);
        }

        return answer;
    }
}