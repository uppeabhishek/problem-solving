from sys import stdin, stdout


def even_sum(nums):
    [a, b] = nums
    a, b = int(a), int(b)
    [a, b] = [b, a] if b < a else [a, b]
    even1, even2, odd1, odd2 = a >> 1, b >> 1, a >> 1, b >> 1
    if a & 1 == 1:
        odd1 += 1
    if b & 1 == 1:
        odd2 += 1

    return (even1 * even2) + (odd1 * odd2)


n = int(stdin.readline())
for _ in range(n):
    stdout.write(str(even_sum(stdin.readline().rstrip().split(" "))) + "\n")
    stdout.flush()
