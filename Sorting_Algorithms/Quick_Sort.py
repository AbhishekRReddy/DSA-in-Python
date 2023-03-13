def swap(nums, index1, index2):
    nums[index1], nums[index2] = nums[index2], nums[index1]

def pivot_func(nums, pivot, last_index):
    swap_index = pivot
    for i in range(pivot+1,last_index+1):
        if nums[i] < nums[pivot]:
            swap_index +=1
            swap(nums,swap_index,i)
    swap(nums,pivot,swap_index)
    return swap_index

nums = [3,5,0,6,2,1,4]
print(pivot_func(nums,0,len(nums)-1))
print(nums)

