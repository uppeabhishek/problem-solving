class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        def bsearch(low, high):
                        
            if low == high:
                return nums[low]
            
            mid = low + (high - low) // 2
            
            if nums[mid] <= nums[low] and nums[mid] <= nums[high]:
                if nums[mid] < nums[mid - 1] and nums[mid] < nums[mid + 1]:
                    return nums[mid]
                if nums[mid - 1] < nums[mid + 1]:
                    return bsearch(low, mid - 1) 

                return bsearch(mid + 1, high)

            elif nums[mid] > nums[low] and nums[mid] > nums[high]:
                if nums[low] < nums[high]:
                    return bsearch(low, mid - 1)
                return bsearch(mid + 1, high)
            elif nums[mid] > nums[low]:
                return bsearch(low, mid - 1)
            return bsearch(mid + 1, high)
            
        return bsearch(0, n - 1)
            
        