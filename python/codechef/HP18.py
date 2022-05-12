from sys import stdin, stdout


def lucky_number(a, b, nums):
    a_cnt, b_cnt, c_cnt = 0, 0, 0
    for i, num in enumerate(nums):
        if num % a == 0 and num % b == 0:
            c_cnt += 1
        elif num % a == 0:
            a_cnt += 1
        elif num % b == 0:
            b_cnt += 1

    if c_cnt > 0:
        a_cnt += 1

    if a_cnt > b_cnt:
        return "BOB"

    return "ALICE"


if __name__ == "__main__":
    n = int(stdin.readline())
    for _ in range(n):
        [_, a1, b1] = list(map(int, stdin.readline().rstrip().split(" ")))
        stdout.write(str(lucky_number(a1, b1, list(map(int, stdin.readline().rstrip().split(" "))))) + "\n")
        stdout.flush()
