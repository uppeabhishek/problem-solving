def print_all_subsequences(string):
    result = []
    for i in range(1, 2 ** len(string)):
        current = bin(i)[2:].zfill(len(string))
        res = []
        for i1, c in enumerate(current):
            if c == '1':
                res.append(string[i1])
        result.append("".join(res))
    print(result)


def helper(index, current, string, result):
    if index == -1:
        result.append(current)
        return

    helper(index - 1, string[index] + current, string, result)
    helper(index - 1, current, string, result)


def print_all_subsequences_recursive(string):
    # 0123 012 013
    result = []
    helper(len(string) - 1, "", string, result)
    print(result)


# print_all_subsequences("aaa")
# print_all_subsequences_recursive("abcd")
print_all_subsequences_recursive("aaa")
