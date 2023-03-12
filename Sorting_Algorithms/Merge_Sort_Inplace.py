def merge(list, start, end):
    mid = (start + end) // 2
    left = []
    right = []
    for i in range(start, mid):
        left.append(list[i])
    for i in range(mid, end):
        right.append(list[i])
    i = 0
    j = 0
    k = start
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            list[k] = left[i]
            i += 1
        else:
            list[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        list[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        list[k] = right[j]
        j += 1
        k += 1
def merge_sort(list, start, end):
    if start == end-1: #This is necessary as the code will enter the infinite recursion
        return
    mid = (start + end) // 2
    merge_sort(list, start, mid)
    merge_sort(list, mid, end)
    merge(list, start, end)

list = [4, 1, 3, 8, 5, 2]
merge_sort(list, 0, len(list))
print(list)
