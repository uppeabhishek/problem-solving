from sys import stdin, stdout


def format_output(nums):
    return " ".join(map(str, nums))


def adj_love(nums):
    odd, even = [], []
    for ele in nums:
        if ele & 1 == 0:
            even.append(ele)
        else:
            odd.append(ele)

    if len(even) == 0:
        if len(odd) % 2 == 0:
            return format_output(odd)
        return -1
    elif len(odd) <= 1:
        return -1
    else:
        if len(odd) % 2 == 0:
            return format_output(odd + even)
        else:
            return format_output(odd[0:-1] + even + [odd[-1]])


n = int(stdin.readline())
for _ in range(n):
    stdin.readline()
    stdout.write(str(adj_love(list(map(int, stdin.readline().rstrip().split(" "))))) + "\n")
    stdout.flush()
