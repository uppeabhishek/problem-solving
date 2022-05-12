from sys import stdin, stdout


def eco_class(nums1, nums2):
    result = 0
    for i in range(len(nums1)):
        if nums1[i] == nums2[i]:
            result += 1
    return result


if __name__ == "__main__":
    n = int(stdin.readline())
    for _ in range(n):
        stdin.readline()
        n1 = list(map(int, stdin.readline().rstrip().split(" ")))
        n2 = list(map(int, stdin.readline().rstrip().split(" ")))
        stdout.write(str(eco_class(n1, n2)) + "\n")
        stdout.flush()
