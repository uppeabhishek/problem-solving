from sys import stdin, stdout


def transform(bullets):
    x, y, z = bullets
    res = z - (y // x)
    return res if res >= 0 else 0


if __name__ == "__main__":
    n = int(stdin.readline())
    for i in range(n):
        stdout.write(str(transform(list(map(int, stdin.readline().rstrip().split(" "))))) + "\n")
        stdout.flush()
