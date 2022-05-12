from sys import stdin, stdout


def chef_and_board_games(current):
    res = 0
    while current >= 0:
        res += current * current
        current -= 2
    return res


n = int(stdin.readline())
for _ in range(n):
    stdout.write(str(chef_and_board_games(int(stdin.readline()))) + "\n")
    stdout.flush()

"""
5
1
2
8
10
1000
"""
