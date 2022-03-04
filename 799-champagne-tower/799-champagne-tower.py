class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if poured == 0:
            return 0

        dp = [[0 for _ in range(j)] for j in range(1, query_row + 3)]
        dp[0][0] = poured

        for i in range(query_row):
            for j in range(i + 1):
                remaining = (dp[i][j] - 1) / 2
                if remaining > 0:
                    dp[i + 1][j] += remaining
                    dp[i + 1][j + 1] += remaining
        return min(1, dp[query_row][query_glass])