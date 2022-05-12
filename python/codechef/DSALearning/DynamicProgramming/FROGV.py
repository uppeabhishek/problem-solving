from sys import stdin, stdout

dic = {}


def precompute():
    cnt = 1
    dic[new_nums[0]] = cnt

    for i, ele in enumerate(new_nums):
        if i == 0:
            continue
        if new_nums[i] - new_nums[i - 1] <= K:
            dic[new_nums[i]] = cnt
        else:
            cnt += 1
            dic[new_nums[i]] = cnt


def chef_and_frogs(n):
    x, y = n
    return "Yes" if dic[nums[x - 1]] == dic[nums[y - 1]] else "No"


N, K, P = list(map(int, (stdin.readline().rstrip().split())))
nums = list(map(int, (stdin.readline().rstrip().split())))
new_nums = sorted(nums)
dp = [0] * (N + 1)
precompute()

for _ in range(N):
    stdout.write(str(chef_and_frogs(list(map(int, (stdin.readline().rstrip().split()))))) + "\n")
    stdout.flush()
