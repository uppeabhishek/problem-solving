from collections import defaultdict


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        arr = sorted(list(s), reverse=True)
        new_arr = []
        dic = defaultdict(int)
        cur = ""
        for i in range(len(arr)):
            if arr[i] != cur:
                new_arr.append(arr[i])
                cur = arr[i]
            dic[arr[i]] += 1

        if len(new_arr) == 1:
            return s

        i, j = 0, 1

        limit = repeatLimit

        result = []

        while i < len(new_arr):
            if dic[new_arr[i]] == 0:
                i = j
                j += 1
                limit = repeatLimit
            else:
                if limit == 0:
                    if j < len(new_arr):
                        if dic[new_arr[j]] > 0:
                            result.append(new_arr[j])
                            dic[new_arr[j]] -= 1
                            limit = repeatLimit
                        else:
                            j += 1
                    else:
                        break
                else:
                    result.append(new_arr[i])
                    dic[new_arr[i]] -= 1
                    limit -= 1

        return "".join(result)


s = Solution()
s.repeatLimitedString("cczazcc", 3)
s.repeatLimitedString("aababab", 2)
s.repeatLimitedString("eeeeedcb", 2)
