# brute force
# we just search each element in the array and see if it equals target, if it is, we will store the index.
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first,last = -1, -1 # set the default value to be -1
        for i in(range(len(nums))): # search each elment in the array
            if nums[i] == target: # first we check if the value is eqaul to target, if not, we just do nothing and start with the next elment
                                  # if the value is equal to the target, then we will further check if this is the first position
                if first == -1: # if first is still equals to -1, means it's still the default value
                    first = i # we can assign the current index to first
                else: # if it's not, we store the index to the next variable
                    last = i #so that during the iteration, we will keep replace the last position with the larger index untill we've search the last element in array
        # after the search, there are three situations, 
        # 1:we find the target and it only appeared once in the array so we have our first index, but the last is still -1,we will return [f,f]
        # 2. we have multiple target value in the array, so we can just 
        if nums.count(target) == 1:
            return [first,first]
        else:
            return [first,last]

# binary search
class Solution:
    def searchRange(self,nums,target):
        left = self.findleft(nums, target) # 最后写这里 let get the left by calling the findleft function, pass in nums, the target
        right = self.findright(nums,target)
        return [left,right] # and then we can return our left and right pointers
                        # by default, if we can't find the result in the functions, it's going to return negative one

    def findleft(self,nums,target): # let's define our two helper functions, the first one is called find left, this will find the left boundary,
                                    # what we need to passed in is the array, and target
        if not nums: # we can chekc the edge case first, if nums is None
            return -1
        left = 0
        right = len(nums) -1 # set the left and right to the beginning of the array and the end of the array

        while left + 1 < right: # we will keep going while our left is less than right minus 1
            mid = (left +right) //2 # first we compute the mid index - left plus right divided by two, we use double slash here for integer division
            if nums[mid] > target: # we can start to compare the mid value to the target:
                right = mid
            elif nums[mid] == target:
                right = mid
            else: #if nums[mid] < target:
                left = mid
        if nums[left] == target:
            return left
        if nums[right] ==target:
            return right
        return -1 # when this while loop ends, we didn't found anything, that means the target value does not exist, we'll just return -1

    def findright(self,nums,target): # we basicly can do the same for the right bounary
        if not nums:
            return -1
        left = 0
        right = len(nums) - 1 # set the left and right to the beginning of the array and the end of the array

        while left + 1 < right:
            mid = (left + right) //2
            if nums[mid] > target:
                right = mid
            elif nums[mid] == target:
                left = mid
            else: # if nums[mid] < target:
                left = mid
        if nums[right] == target:
            return right
        if nums[left] == target:
            return left
        return -1
