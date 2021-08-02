# brute force
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        f,s = -1, -1
        
        for i in(range(len(nums))):
            if nums[i] == target:
                if f == -1: # make sure we get the first value
                    f = i
                else:
                    s = i
        if nums.count(target) == 1:
            return [f,f]
        else:
            return [f,s]

# binary search
class Solution:
    def searchRange(self, nums, target):
        l = self.findLeft(nums, target)
        r = self.findRight(nums, target)
        if left <= right:
            return [left,right]
        else:
            return [-1,-1]
    
    
    def findLeft(self, nums, target):
        l, mid, r = 0, 0, len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l    # 比Target大的最小值

        
    def findRight(self, nums, target):
        l, mid, r = 0, 0, len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
        return r #比Target小的最大值
