from sys import stdin, stdout


def inc_iq(num):
    return "YES" if num + 7 > 170 else "NO"


if __name__ == "__main__":
    stdout.write(str(inc_iq(int(stdin.readline().rstrip()))) + "\n")
    stdout.flush()
