from sys import stdin, stdout


def eq_differ(nums):
    if len(nums) < 3:
        return 0
    nums.sort()

    cnt = 1
    result = 0

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            result = max(result, cnt)
            cnt = 1
        else:
            cnt += 1


if __name__ == "__main__":
    n = int(stdin.readline())
    for _ in range(n):
        stdin.readline()
        stdout.write(str(eq_differ(list(map(int, stdin.readline().rstrip().split(" "))))) + "\n")
        stdout.flush()
