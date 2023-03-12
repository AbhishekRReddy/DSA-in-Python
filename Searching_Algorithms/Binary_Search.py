def binary_search(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high)//2
        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return 'Element does not Exists'
nums = [1,2,3,4,5,6,7,8,9]
print(binary_search(nums, 10))