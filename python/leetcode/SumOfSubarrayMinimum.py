from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:

        n = len(arr)
        stack = []
        result = []

        for i in range(n):

            while len(stack) and arr[i] <= arr[stack[-1]]:
                stack.pop()

            stack.append(i)
            top = stack[-1]

            if len(stack) == 1:
                result.append(arr[top] * (i + 1))
            else:
                next_top = stack[-2]
                if i - next_top == 1:
                    result.append(arr[top] * (i - next_top) + result[top - 1])
                else:
                    result.append(arr[top] * (i - next_top) + result[next_top])

        return sum(result)


s = Solution()
s.sumSubarrayMins([3, 1, 2, 5, 4])
s.sumSubarrayMins([3, 1, 2, 4])
s.sumSubarrayMins([11, 81, 94, 43, 3])
