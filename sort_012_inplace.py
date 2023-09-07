# This code sorts 0, 1, 2 numbers present in an array in place
# This uses pointer approach
def sort_numers_in_place(nums):
    left = 0
    right = len(nums) - 1
    mid = 0
    
    while mid <= right:
        # if nums[mid] is 0 increment both mid and left and swap both mid and left
        if nums[mid] == 0:
            nums[left], nums[mid] = nums[mid], nums[left]
            left += 1
            mid += 1
        # If nums[mid] is 1 then dont increment left, just increment mid
        elif nums[mid] == 1:
            mid += 1
        # if nums[mid] is 2 then decrease right and swap mid and right
        else:
            nums[right], nums[mid] = nums[mid], nums[right]
            right -= 1
    return nums

nums = [0,1,1,0,2,1]

print(sort_numers_in_place(nums))
        
