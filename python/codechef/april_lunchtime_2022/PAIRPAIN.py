from sys import stdin, stdout


def pair_pain(pair):
    ones = 0
    twos = 0
    new_array = []
    for i, p in enumerate(pair):
        if p == 1:
            ones += len(pair) - i - 1
            if len(new_array):
                new_array.append(p)
        elif p == 2:
            new_array.append(p)

    for i, ele in enumerate(new_array):
        if ele == 2:
            twos += len(new_array) - i - 1

    return ones + twos


if __name__ == "__main__":
    n = int(stdin.readline())
    for _ in range(n):
        stdin.readline()
        stdout.write(str(pair_pain(list(map(int, stdin.readline().rstrip().split(" "))))) + "\n")
        stdout.flush()

"""
1
5
1 3 4 1 5 8 2 3 1 2 1 1 2 1 3 3 1
"""
