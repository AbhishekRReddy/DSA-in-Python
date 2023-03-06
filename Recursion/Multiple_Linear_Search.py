def recursive_search(numbers, value, index = 0, index_list=[]):
    if index == len(numbers):
        return index_list
    if numbers[index] == value:
        index_list.append(index)
    return recursive_search(numbers, value, index+1, index_list)

numbers = [10,20,30,40,50,60,70,80,20,30,20,40,20,20,]
print(numbers)
print(recursive_search(numbers, 20))