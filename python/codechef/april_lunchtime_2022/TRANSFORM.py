from sys import stdin, stdout


def transform(mario_size):
    mario_size = mario_size % 3
    if mario_size == 0:
        return "NORMAL"
    elif mario_size == 1:
        return "HUGE"
    else:
        return "SMALL"


if __name__ == "__main__":
    n = int(stdin.readline())
    for i in range(n):
        stdout.write(str(transform(int(stdin.readline()))) + "\n")
        stdout.flush()
