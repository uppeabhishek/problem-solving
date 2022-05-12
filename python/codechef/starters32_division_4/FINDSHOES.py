from sys import stdin, stdout


def find_shoes(nums):
    N, M, = nums
    return N * 2 - (min(N, M))


n = int(stdin.readline())
for _ in range(n):
    stdout.write(str(find_shoes(list(map(int, (stdin.readline().rstrip().split()))))) + "\n")
    stdout.flush()
