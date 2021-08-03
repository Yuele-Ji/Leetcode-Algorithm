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
        
        if nums.count(target) == 1: # after the for loop
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

class Solution:
def searchRange(self,nums,target):
    left = self.findleft(nums, target) # 最后写这里 let get the left by calling the findleft function, pass in nums, the target
    right = self.findright(nums,target)
    return [left,right] # and then we can return our left and right pointers
                        # by default, if we can't find the result in the functions, it's going to return negative one

def findleft(self,nums,target): # let's define our two helper functions, the first one is called find left, this will find the left boundary,
                                  what we need to passed in is the array, and target
    if not nums:
        return -1
    left = 0
    right = len(nums) -1 # set the left and right to the beginning of the array and the end of the array

    while left < right -1 : # we will keep going while our left is less than right minus 1
        mid = (left +right) //2 # first we compute the mid index - left plus right divided by two, we use double slash here for integer division
        if nums[mid] > target:
            right = mid
        if nums[mid] == target:
            right = mid
        if nums[mid] < target:
            left = mid
    if nums[left] ==target:
        return left
    if nums[right] ==target:
        return right
    return -1 # when this while loop ends, we didn't found anything, that means the target value does not exist, we'll just return -1

def findright(self,nums,target):
    if not nums:
        return -1
    left = 0
    right = len(nums) - 1 # set the left and right to the beginning of the array and the end of the array

    while left < right -1:
        mid = (left + right) //2
        if nums[mid] > target:
            right = mid
        if nums[mid] == target:
            left = mid
        if nums[mid] < target:
            left = mid
    if nums[right] == target:
        return right
    if nums[left] == target:
        return left
    return -1
