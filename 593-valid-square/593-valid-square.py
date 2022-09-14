from math import sqrt

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        
        
        def getDistance(x, y):
            x1, y1 = x
            x2, y2 = y
            return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        
        def checkIfEqual(first, second, third, fourth):
            
            first, second, third, fourth, diagonal1, diagonal2 = getDistance(first, second), getDistance(second, third), getDistance(third, fourth), getDistance(fourth, first), getDistance(first, third), getDistance(second, fourth)
                        
            return (first == second == third == fourth) and (diagonal1 == diagonal2) and first > 0 and diagonal1 > 0
        
        
        actual_list = [p1, p2, p3, p4]

        def swap(arr, i, j):
            arr[i], arr[j] = arr[j], arr[i]
        
        def permutations(arr, l, r):
            
            nonlocal actual_list
            
            if l == r:
                if checkIfEqual(actual_list[arr[0]], actual_list[arr[1]], actual_list[arr[2]], actual_list[arr[3]]):
                    return True
                return False
            
            for i in range(l, r):
                swap(arr, i, l)
                if permutations(arr, l + 1, r):
                    return True
                swap(arr, i, l)
            
            return False
                
        return permutations([0, 1, 2, 3], 0, 4)
        
        
        
        