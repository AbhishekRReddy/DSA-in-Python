def Insertion_Sort(array):
    for i in range(1, len(array)):
        key = array[i] #This is the element I want INSERT in the left subarray
        j = i-1 #From here the sorted array will be there
        while j>=0 and key < array[j]:
            array[j+1] = array[j] #Moving every element in the left sub array one position left
            j -= 1
        #When we reach this line, because of 2 reasons:
            #1: j= -1 means key is less than all the elements
            #2: We have reached a position where its ideal to insert the element key
        array[j+1] = key
        #Why j+1 ? We have already decremeneted and while condition failing when j is pointing certain element
        #which is greater than the key. So we want to insert in the next position of such element.


list = [2,2,4,0,5,7,3,2,1,9,10]
Insertion_Sort(list)
print(list)
