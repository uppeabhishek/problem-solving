from sys import stdin, stdout


def split_pair(num):
    if num < 10:
        return "NO"

    last_digit = None

    while num:
        rem = num % 10
        if last_digit is None:
            last_digit = 0 if (rem % 2 == 0) else 1
        else:
            if last_digit == 0:
                if rem % 2 == 0:
                    return "YES"
            else:
                if rem % 2 == 1:
                    return "YES"
        num = num // 10

    return "NO"


n = int(stdin.readline())
for _ in range(n):
    stdout.write(str(split_pair(int(stdin.readline()))) + "\n")
    stdout.flush()
