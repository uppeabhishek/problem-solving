from collections import Counter


class Solution:

    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ''

        min_len = len(s)

        actual_set = Counter(t)
        t_set = Counter(t)

        prev_i = 0
        i = 0

        while i < len(s):
            if s[i] in t_set and t_set[s[i]]:
                t_set[s[i]] -= 1
                if t_set[s[i]] == 0:
                    del t_set[s[i]]

            if not len(t_set):
                min_len = min(min_len, i - prev_i + 1)
                prev_value = s[prev_i]
                prev_i += 1
                i += 1
                while i < len(s) and s[i] != prev_value:
                    if s[i] in actual_set:
                        t_set[s[i]] += 1
                    i += 1
                print(i)
                break

            i += 1


s = Solution()
s.minWindow("ADOBECODEBANC", "ABC")
