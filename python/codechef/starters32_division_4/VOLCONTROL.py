from sys import stdin, stdout


def vol_control(nums):
    a, b = nums
    return abs(a - b)


N = int(stdin.readline())
for _ in range(N):
    stdout.write(str(vol_control(list(map(int, (stdin.readline().rstrip().split()))))) + "\n")
    stdout.flush()
