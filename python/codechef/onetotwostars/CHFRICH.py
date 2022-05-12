from sys import stdin, stdout


def richie_rich(li):
    A, B, X = li
    return (B - A) // X


if __name__ == "__main__":
    n = int(stdin.readline())
    for _ in range(n):
        stdout.write(str(richie_rich(list(map(int, (stdin.readline().rstrip().split()))))) + "\n")
        stdout.flush()
