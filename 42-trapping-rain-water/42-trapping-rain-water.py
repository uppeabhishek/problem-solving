class Solution:
    def trap(self, height: List[int]) -> int:
        
        if len(height) == 0:
            return 0

        i, j = 0, 1

        result = 0

        while j < len(height):

            while j < len(height) and height[j] < height[i]:
                j += 1

            if j != len(height):
                min_val = min(height[i], height[j])
                if min_val != 0:
                    temp = 0
                    for k in range(i + 1, j):
                        temp += abs(min_val - height[k])
                    result += temp
            else:
                j -= 1
                max_val = height[j]
                temp = 0

                while j >= i:
                    if max_val > height[j]:
                        temp += max_val - height[j]
                    else:
                        max_val = height[j]
                    j -= 1

                result += temp
                break

            i = j
            j += 1

        return result
                
            
            
        