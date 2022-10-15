class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:

        current = []

        for i, worker in enumerate(workers):
            for j, bike in enumerate(bikes):
                distance = abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])
                current.append((distance, i, j))

        current.sort()

        bikes_set = set()

        result = [-1] * len(workers)

        for i, j, k in current:
            if result[j] == -1 and k not in bikes_set:
                bikes_set.add(k)
                result[j] = k

        return result