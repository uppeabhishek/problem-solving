from sys import stdin, stdout


def alternating_substring(num):
    if num & 1 == 1:
        return -((num + 1) // 2)
    return num // 2


if __name__ == "__main__":
    n = int(stdin.readline())
    for _ in range(n):
        stdout.write(str(alternating_substring(int(stdin.readline().rstrip()))) + "\n")
        stdout.flush()
