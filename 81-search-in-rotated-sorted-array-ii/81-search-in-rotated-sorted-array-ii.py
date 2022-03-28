class Solution:
    
    def bsearch(self, nums, low, high, target):
                
        while low <= high:
            
            mid = (low + high) // 2
            
            if nums[mid] == target or nums[low] == target or nums[high] == target:
                return True
            
            elif nums[mid] < nums[high]:
                if target > nums[mid] and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            elif nums[low] < nums[mid]:
                if target >= nums[low] and target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                low+=1
                high-=1
        return False
                
        
    
    def search(self, nums: List[int], target: int) -> bool:
        return self.bsearch(nums, 0, len(nums)-1, target)