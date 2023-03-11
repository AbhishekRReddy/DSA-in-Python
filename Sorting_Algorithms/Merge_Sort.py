def merge(left,right):
    i = 0
    j = 0
    merged_list=[]
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged_list.append(left[i])
            i += 1
        else:
            merged_list.append(right[j])
            j += 1
    if i < len(left):
        merged_list.extend(left[i:])
    else:
        merged_list.extend(right[j:])
    return merged_list

def merge_sort(list):
    if len(list) == 1:
        return list
    mid = len(list)//2
    left = merge_sort(list[:mid])
    right = merge_sort(list[mid:])
    return merge(left,right)
list=[2,4,1,3,5,6]
print(merge_sort(list))