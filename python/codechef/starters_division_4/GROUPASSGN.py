from sys import stdin, stdout


def group_assignment(nums):
    [a, b] = nums
    return (a * 2) - b + 1


if __name__ == "__main__":
    n = int(stdin.readline())
    for _ in range(n):
        stdout.write(str(group_assignment(list(map(int, stdin.readline().rstrip().split(" "))))) + "\n")
