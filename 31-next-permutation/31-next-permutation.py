class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        while i > 0:
            if nums[i] > nums[i - 1]:
                break
            i -= 1

        if i == 0:
            nums.sort()
        else:
            current = nums[i - 1]
            min_val = math.inf
            min_ind = -1
            for j in range(i, len(nums)):
                if current < nums[j] < min_val:
                    min_val = min(min_val, nums[j])
                    min_ind = j

            nums[i - 1], nums[min_ind] = nums[min_ind], nums[i - 1]
            nums[i:] = sorted(nums[i:])
            
                