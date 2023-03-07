def rotation(nums, k):
    while k > 0:
        temp = nums.pop()
        nums.insert(0, temp) 
        k -= 1
    return nums

numms = [1, 2 , 3, 4, 5, 6]
print(rotation(numms, 2))