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

print(max_product([1,2,3,4,5,0]))
