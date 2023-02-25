def binary_search(numbers:int, num:int, low, high):
    mid = (high+low)//2
    if low==high and numbers[mid]!=num:
        print('number does not exist')
        return 

    if(numbers[mid]==num):
        return mid
    elif numbers[mid] < num:
        return binary_search(numbers, num, mid+1,high)
    else:
        return binary_search(numbers, num, low, mid-1)


numbers = [x for x in range(1,11)]
print(numbers)
print(binary_search(numbers, 1, 0 ,len(numbers)-1))






    
