from sys import stdin, stdout


def rating(num):
    return -1 * (num + 1)


if __name__ == "__main__":
    n = int(stdin.readline())
    for i in range(n):
        stdout.write(str(rating(int(stdin.readline()))) + "\n")
        stdout.flush()
