from sys import stdin, stdout


def alternating_substring(num):
    zeros, ones = 0, 0
    for c in num:
        if c == '0':
            zeros += 1
        else:
            ones += 1

    if zeros == ones:
        return zeros + ones
    if zeros < ones:
        return zeros * 2 + 1
    return ones * 2 + 1


if __name__ == "__main__":
    n = int(stdin.readline())
    for _ in range(n):
        stdin.readline()
        stdout.write(str(alternating_substring(stdin.readline().rstrip())) + "\n")
        stdout.flush()
