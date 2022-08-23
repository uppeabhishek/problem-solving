class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:

        n = len(arr)
        stack = []
        result = []
        modulo = 10 ** 9 + 7

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

        return sum(result) % modulo
