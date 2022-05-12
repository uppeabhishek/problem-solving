from sys import stdin, stdout


def lunch_time(time):
    return "YES" if 1 <= time <= 4 else "NO"


if __name__ == "__main__":
    n = int(stdin.readline())
    for i in range(n):
        stdout.write(str(lunch_time(int(stdin.readline()))) + "\n")
        stdout.flush()
