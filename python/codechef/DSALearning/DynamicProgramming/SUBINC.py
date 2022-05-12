from sys import stdin, stdout


def sub_array(nums):
    result = [1] * len(nums)
    for i in range(1, len(nums)):
        if nums[i] >= nums[i - 1]:
            result[i] = result[i - 1] + 1
    return sum(result)


n = int(stdin.readline())
for _ in range(n):
    stdin.readline()
    stdout.write(str(sub_array(list(map(int, stdin.readline().rstrip().split(" "))))) + "\n")
    stdout.flush()
