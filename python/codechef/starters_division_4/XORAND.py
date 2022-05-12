from sys import stdin, stdout


def summation(num):
    return (num * (num - 1)) // 2


def xor_and_and(nums):
    nums.sort()
    same_cnt = 0
    diff_cnt = 0

    start_1, start_2 = True, True

    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            if start_1:
                same_cnt += 1
                start_1 = False
            same_cnt += 1
            start_2 = True
        else:
            if nums[i] > 1 and nums[i + 1] == nums[i] + 1 and (nums[i] & (nums[i] - 1)) == 0:
                if start_2:
                    diff_cnt += 1
                    start_2 = False
                diff_cnt += 1
            start_1 = True

    return summation(same_cnt) + summation(diff_cnt)


if __name__ == "__main__":
    n = int(stdin.readline())
    for _ in range(n):
        stdin.readline()
        stdout.write(str(xor_and_and(list(map(int, stdin.readline().rstrip().split(" "))))) + "\n")
        stdout.flush()
