from sys import stdin, stdout


def three_topics(nums):
    return "Yes" if nums[0] == nums[3] or nums[1] == nums[3] or nums[2] == nums[3] else "No"


if __name__ == "__main__":
    stdout.write(str(three_topics(list(map(int, stdin.readline().rstrip().split(" "))))) + "\n")
    stdout.flush()
