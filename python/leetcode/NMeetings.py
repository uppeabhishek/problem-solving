class Solution:
    def maximumMeetings(self, n, start, end):
        meetings = []
        for i in range(n):
            meetings.append((start[i], end[i]))
        meetings.sort(key=lambda k: k[1])

        last_val = -1

        res = 0

        for meeting in meetings:
            if meeting[0] > last_val:
                last_val = meeting[1]
                res += 1

        return res


s = Solution()
s.maximumMeetings(6, [1, 3, 0, 5, 8, 5], [2, 4, 6, 7, 9, 9])
s.maximumMeetings(3, [10, 12, 20], [20, 25, 30])
