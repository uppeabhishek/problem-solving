class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n + 1):
            cur, cnt = i, 0
            while cur:
                cur = cur & (cur - 1)
                cnt += 1
            result.append(cnt)
            
        return result