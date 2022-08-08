from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = defaultdict(int)

        i = 0
        prev_i = 0
        max_len = 0

        while i < len(s):
            c = s[i]

            if dic[c] == 1:
                max_len = max(max_len, len(dic))

                update_prev_i = True

                while prev_i < i:
                    del dic[s[prev_i]]
                    if s[prev_i] == c:
                        prev_i += 1
                        update_prev_i = False
                        break
                    prev_i += 1

                if update_prev_i:
                    prev_i = i

            dic[c] = 1
            i += 1

        return max(max_len, len(dic))


s = Solution()
s.lengthOfLongestSubstring("aabaab!bb")
