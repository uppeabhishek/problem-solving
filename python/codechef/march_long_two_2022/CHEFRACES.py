from sys import stdin, stdout


def chef_races(nums):
    x, y, a, b = nums[0], nums[1], nums[2], nums[3]
    res = 0
    if x != a and x != b:
        res += 1
    if y != a and y != b:
        res += 1

    return res


if __name__ == "__main__":
    n = int(stdin.readline())
    for i in range(n):
        stdout.write(str(chef_races(list(map(int, stdin.readline().rstrip().split(" "))))) + "\n")
        stdout.flush()
