from sys import stdin, stdout


def geometric_progression(a, r, n):
    return int(a * ((1 - r ** n) / (1 - r)))


def previous_power_of_2(n):
    n |= n >> 1
    n |= n >> 2
    n |= n >> 4
    n |= n >> 8
    n |= n >> 16
    return n ^ (n >> 1)


def get_cnt(num):
    all_ones = True
    cnt = 0
    while num:
        if num & 1 == 0:
            all_ones = False
        num = num >> 1
        cnt += 1
    return all_ones, cnt


def unchanged_dor(num):
    if num == 1:
        return 1

    all_ones, cnt = get_cnt(num)

    if all_ones:
        prev_cnt = cnt - 1
        return geometric_progression(2, 2, prev_cnt) - prev_cnt
    else:
        previous = previous_power_of_2(num)
        _, cnt = get_cnt(previous - 1)
        prev_cnt = cnt - 1
        return (geometric_progression(2, 2, prev_cnt) - prev_cnt) + (num - previous)


if __name__ == "__main__":
    n1 = int(stdin.readline())
    for _ in range(n1):
        stdout.write(str(unchanged_dor(int(stdin.readline().rstrip()))) + "\n")
        stdout.flush()
