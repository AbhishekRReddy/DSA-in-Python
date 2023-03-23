def swap(nums, index1, index2):
    nums[index1], nums[index2] = nums[index2], nums[index1]

#Pivot Function allocates the number to its specified value

def pivot_func(nums, pivot, last_index):
    swap_index = pivot
    for i in range(pivot+1,last_index+1):
        if nums[i] < nums[pivot]:
            swap_index +=1
            swap(nums,swap_index,i)
    swap(nums,pivot,swap_index)
    return swap_index
 
def quick_sort(nums,left,right):
    if left == right:
        return
    pivot_index = pivot_func(nums,left,right)
    quick_sort(nums,left,pivot_index-1)
    quick_sort(nums,pivot_index+1,right)

nums = [3,5,0,6,2,1,4]
print(quick_sort(nums, 0 ,len(nums)-1))
print(nums)

