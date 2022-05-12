from sys import stdin, stdout


def cred_coins(current):
    return (int(current[0]) * int(current[1])) // 100


n = int(stdin.readline())
for _ in range(n):
    stdout.write(str(cred_coins(stdin.readline().rstrip().split(" "))) + "\n")
    stdout.flush()
