class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def bsearch(low, high):
                        
            if low > high:
                return -1
            
            mid = (low + high) // 2
            
            if nums[mid] == target:
                return mid
            else:
                
                first, second = False, False
            
                if nums[low] <= nums[mid]:
                    if nums[low] <= target <= nums[mid]:
                        return bsearch(low, mid - 1)
                    first = True
                
                elif nums[mid] <= nums[high]:
                    if nums[mid] <= target <= nums[high]:
                        return bsearch(mid + 1, high)
                    second = True
                
                if not first:
                    return bsearch(low, mid - 1)
                
                if not second:
                    return bsearch(mid + 1, high)
                
                                        
        return bsearch(0, len(nums) - 1)
        