from sys import stdin, stdout


def broken_phone(nums):
    se = set()
    for i in range(len(nums) - 1):
        if nums[i] != nums[i + 1]:
            se.add(i)
            se.add(i + 1)
    return len(se)


n = int(stdin.readline())
for _ in range(n):
    stdin.readline()
    stdout.write(str(broken_phone(stdin.readline().rstrip().split(" "))) + "\n")
    stdout.flush()
