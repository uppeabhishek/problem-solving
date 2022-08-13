class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        min_val = sys.maxsize
        min_res = sys.maxsize
        
        for i in range(len(nums)):
            
            first = nums[i]        
            
            i1, j1 = i + 1, len(nums) - 1

            while i1 < j1:

                second, third = nums[i1], nums[j1]

                current_sum = first + second + third

                if current_sum == target:
                    return target   
                else:
                    diff = abs(current_sum - target)

                    if diff < min_val:
                        min_val = diff
                        min_res = current_sum

                    if current_sum < target:
                        i1 += 1
                    else:
                        j1 -= 1
            
        return min_res