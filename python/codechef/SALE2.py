from sys import stdin, stdout


def sale2(items):
    i1, i2 = int(items[0]), int(items[1])
    return (i1 - (i1 // 3)) * i2


n = int(stdin.readline())
for _ in range(n):
    stdout.write(str(sale2(stdin.readline().rstrip().split(" "))) + "\n")
    stdout.flush()
