class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 1

        intervals.sort(key=lambda k: (k[0], -k[1]))

        prev = 0
        cnt = 0

        for i in range(1, len(intervals)):
            if intervals[i][0] >= intervals[prev][0] and intervals[i][1] <= intervals[prev][1]:
                cnt += 1
            else:
                prev = i

        return len(intervals) - cnt