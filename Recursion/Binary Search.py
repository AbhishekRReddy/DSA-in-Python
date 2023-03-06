def core_binary_search(numbers:int, num:int, low=0, high=0,first_call = True):
    if first_call:
        high = len(numbers)
    mid = (high+low)//2
    if low==high and numbers[mid]!=num:
        print('number does not exist')
        return 
    if(numbers[mid]==num):
        return mid
    elif numbers[mid] < num:
        return core_binary_search(numbers, num, low = mid+1,high = high, first_call= False)
    else:
        return core_binary_search(numbers, num, low, high = mid-1, first_call= False)



numbers = [x for x in range(1,11)]
print(numbers)
print(core_binary_search(numbers, 1))






    
