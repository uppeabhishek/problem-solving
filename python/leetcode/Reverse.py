class Solution:
    def reverse(self, x: int) -> int:
        result = 0

        negative = False
        if x < 0:
            negative = True
            x = x * -1

        while x != 0:
            rem = x % 10
            result = result * 10 + rem
            x = x // 10

        if negative:
            result = result * -1
            if result < -2 ** 31:
                return 0
        else:
            if result > 2 ** 31 - 1:
                return 0

        return result

s = Solution()
s.reverse(-123)
