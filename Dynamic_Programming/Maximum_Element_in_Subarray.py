def max_product(nums):
    global_max = 0
    #We are checking for all the possible sub-arrays.
    for x,i in enumerate(nums,0):
        local_max = i
        sub_array =[i]
        for j in range(x+1, len(nums)):
            sub_array.append(nums[j])
            print(sub_array)
            local_max = local_max*nums[j]
            global_max = max(global_max, local_max)
    return global_max


#Two traversals method
'''
If zero is countered we are resetting the subarray. Suppose if one zero is present inside the array
then there will two subarrays on either side of the zero
[-2,-1,3,0,-4]
At the end we are comparaing the max_left and max_right with zero also because zero is also one subarray
and two subarrays product can be negatives
'''

def max_product_two_traverse(nums):
    max_left = nums[0]
    max_right = nums[0] #Choose any of the element in the given array
    is_zero_encounterd = False
    prod = 1
    for n in nums:
        prod *= n
        if n == 0:
            is_zero_encounterd = True #Refer to above why we are using the is_zero_encoutnered
            prod = 1
            continue
        max_left = max(max_left, prod)
    prod = 1
    for n in reversed(nums):
        prod *= n
        if n == 0:
            is_zero_encounterd = True
            prod = 1
            continue
        max_right = max(max_right, prod)
    if is_zero_encounterd:
        return max(max(max_left,max_right), 0) #Considering the subarrau of the zero
    return max(max_right,max_left)


print(max_product_two_traverse([-2,-1,-3,0,-4]))