from sys import stdin, stdout


def cri_cup(nums):
    [a, b, d] = nums
    if abs(a - b) <= d:
        return "YES"
    return "NO"


if __name__ == "__main__":
    n = int(stdin.readline())
    for _ in range(n):
        stdout.write(str(cri_cup(list(map(int, stdin.readline().rstrip().split(" "))))) + "\n")
        stdout.flush()
