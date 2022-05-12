from sys import stdin, stdout

MOD = 1000000009

res = [0] * 1000001
res[2] = 1
res[3] = 1


def billiards(num):
    if num < 2:
        return 0

    if res[num]:
        return res[num]

    for i in range(4, num + 1):
        res[i] = ((res[i - 2] % MOD) + (res[i - 3] % MOD)) % MOD

    return res[num]


n = int(stdin.readline())
for _ in range(n):
    stdout.write(str(billiards(int(stdin.readline()))) + "\n")
    stdout.flush()
