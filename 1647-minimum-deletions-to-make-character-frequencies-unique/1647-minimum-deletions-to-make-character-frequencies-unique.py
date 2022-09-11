class Solution:
    def minDeletions(self, s: str) -> int:
        arr = sorted(list(Counter(s).values()), reverse = True)
        result = 0
                
        for i in range(len(arr) - 1):
            diff = arr[i + 1] - arr[i]
            if diff == 0:
                arr[i + 1] = arr[i] - 1
                result += 1
            elif diff > 0:
                if arr[i] == 0:
                    result += diff
                    arr[i + 1] = 0
                else:
                    result += diff + 1
                    arr[i + 1] = arr[i + 1] - diff - 1        

        return result