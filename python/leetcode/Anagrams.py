from collections import defaultdict, Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        p_counter = defaultdict(set)

        actual_counter = Counter(p)

        def isCounterMatched():
            if len(p_counter) != len(actual_counter):
                return False

            for key, value in p_counter.items():
                if key not in actual_counter or actual_counter[key] != len(value):
                    return False

            return True

        def helper():

            nonlocal p_counter, actual_counter

            result = []

            i = 0

            while i < len(s):

                current = s[i]

                fail_condition = current not in actual_counter or actual_counter[current] == 0

                if fail_condition:
                    p_counter = defaultdict(set)
                else:
                    p_counter[current].add(i)

                    if len(p_counter[current]) > actual_counter[current]:
                        first = min(p_counter[current])
                        prev_result = result[-1] if len(result) else 0

                        for c in range(prev_result, first + 1):
                            if s[c] in p_counter and c in p_counter[s[c]]:
                                p_counter[s[c]].remove(c)

                if isCounterMatched():
                    prev = i + 1 - len(p)
                    result.append(prev)

                i += 1

            print(result)
            return result

        helper()


s = Solution()
s.findAnagrams("bacdgabcda", "abcd")
