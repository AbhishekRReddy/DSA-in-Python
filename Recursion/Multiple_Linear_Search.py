
def recursive_search(numbers, value, index = 0, index_list=[]):
    if index == len(numbers):
        return index_list
    if numbers[index] == value:
        index_list.append(index)
    return recursive_search(numbers, value, index+1, index_list)

#Using the list inside the function body
def recursive_search_2(numbers, value, index =0):
    a =[]
    if index == len(numbers):
        return a
    if numbers[index] == value:
        a.append(index)
    return a + recursive_search_2(numbers, value, index+1)


numbers = [10,20,30,40,50,60,70,80,20,30,20,40,20,20,]
print(numbers)
list = recursive_search_2(numbers, 20)
print(list)