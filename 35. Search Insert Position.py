class Solution:
    def searchInsert(self, nums:List[int], target:int) -> int:
        left = 0
        right = len(nums) # we might need to inseart at the end
        
        while left < right:
            mid = left + (right - left) // 2 # avoids overflow
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid  # it might be possibe to inseart @ mid
            else:
                left = mid + 1 # no way mid is a valid option
        return left
