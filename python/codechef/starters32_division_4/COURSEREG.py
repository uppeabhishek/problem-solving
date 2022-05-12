from sys import stdin, stdout


def course_reg(nums):
    N, M, K = nums
    return "Yes" if N <= M - K else "No"


n = int(stdin.readline())
for _ in range(n):
    stdout.write(str(course_reg(list(map(int, (stdin.readline().rstrip().split()))))) + "\n")
    stdout.flush()
