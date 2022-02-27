class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        low, high = 1, min(time) * totalTrips
        res = math.inf
        while low <= high:
            mid = low + (high - low) // 2
            result = 0
            for t in time:
                result += mid // t
            if result >= totalTrips:
                res = min(res, mid)
                high = mid - 1
            else:
                low = mid + 1
        return res