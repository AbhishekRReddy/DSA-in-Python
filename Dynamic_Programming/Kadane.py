#Kadane's algorithm gives the maximum product of the sub array

def kadanes(nums):
    '''
    we have 3 choiced to choose
    1. The number itself
    2.The number * maximum negative number
    3. The number * maximum positive number
    '''
    max_prod = nums[0]
    min_prod = nums[0]
    result = nums[0]
    for i in range(1,len(nums)):
        choice1 = max_prod * nums[i]
        choice2 = min_prod * nums[i]
        max_prod = max(nums[i], max(choice1,choice2))
        min_prod = min(nums[i], min(choice1,choice2))
        result = max(max_prod,result)
    return result

print(kadanes([1,2,-3,0,-4,-5]))

