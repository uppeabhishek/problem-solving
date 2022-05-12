from sys import stdin, stdout


def min_coins(coins):
    if coins % 5 != 0:
        return -1
    ten = coins // 10
    five = (coins - (ten * 10)) // 5
    return ten + five


n = int(stdin.readline())
for _ in range(n):
    stdout.write(str(min_coins(int(stdin.readline()))) + "\n")
    stdout.flush()
