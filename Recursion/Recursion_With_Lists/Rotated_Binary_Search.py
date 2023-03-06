def rotated_binary_search(numbers, target, start, end):
    if start > end:
        return
    mid = (start + end)//2
    if numbers[mid] == target:
        return mid
    else:
        if numbers[mid] <= numbers[end]:
            if target > numbers[mid] and target <= numbers[end]:
                return rotated_binary_search(numbers, target, mid+1, end)
            else:
                return rotated_binary_search(numbers, target, start, mid-1)
        else:
            if target >= numbers[start] and target < numbers[mid]:
                return rotated_binary_search(numbers, target, start, mid-1)
            else:
                return rotated_binary_search(numbers, target, mid+1, end)


num = [7,6,5,4,3,2,1]
print(rotated_binary_search(num, 1, 0, len(num)-1))
